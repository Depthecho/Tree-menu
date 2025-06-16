from django import template
from django.urls import resolve, reverse, NoReverseMatch
from ..models import Menu, MenuItem
from django.db.models import Prefetch

register = template.Library()


# Вспомогательный inclusion_tag для рекурсивного рендеринга дочерних элементов
@register.inclusion_tag('menu_app/_menu_recursive.html', takes_context=True)
def draw_menu_recursive(context, menu_items, active_path_ids, active_item_id):
    # Передаем весь контекст, чтобы у нас был доступ к request в рекурсивном шаблоне
    return {
        'menu_items': menu_items,
        'active_path_ids': active_path_ids,
        'active_item_id': active_item_id,
        'request': context['request']
    }


# Основной inclusion_tag, который будет вызываться в шаблонах Django: {% draw_menu 'main_menu' %}
@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path  # Текущий URL-путь страницы

    # Получаем все пункты меню для данного имени в ОДИН ЗАПРОС к БД.
    try:
        # Получаем объект Menu по имени
        menu = Menu.objects.get(name=menu_name)

        # Получаем все MenuItem, связанные с этим Menu.
        all_menu_items = MenuItem.objects.filter(menu=menu).order_by('id')

        # Строим словарь для быстрого доступа к элементам по ID
        item_map = {item.id: item for item in all_menu_items}

        # Определяем корневые элементы и строим иерархию (добавляем 'children_list' к объектам)
        root_items = []
        for item in all_menu_items:
            item.children_list = []  # Добавляем атрибут для хранения прямых потомков
            if item.parent_id is None:
                root_items.append(item)
            else:
                parent_item = item_map.get(item.parent_id)
                if parent_item:
                    parent_item.children_list.append(item)

        # Определяем активный пункт и путь до него
        active_item = None
        active_path_ids = set()  # Множество ID элементов в пути от корня до активного

        # Нормализуем текущий путь, чтобы корректно сравнивать
        normalized_current_path = current_path
        if normalized_current_path != '/' and normalized_current_path.endswith('/'):
            normalized_current_path = normalized_current_path[:-1]

        # Ищем наиболее специфичный активный пункт
        for item in all_menu_items:
            item_url = item.get_absolute_url()

            # Нормализуем URL пункта меню
            normalized_item_url = item_url
            if normalized_item_url != '/' and normalized_item_url.endswith('/'):
                normalized_item_url = normalized_item_url[:-1]

            # Проверяем, является ли текущий URL началом URL пункта меню
            if normalized_current_path.startswith(normalized_item_url) and normalized_item_url:
                # Если найдено совпадение, проверяем, является ли оно более специфичным (более длинным)
                if active_item is None or len(normalized_item_url) > len(active_item.get_absolute_url().strip('/')):
                    active_item = item

        # Если активный элемент найден, строим путь от него до корня
        if active_item:
            current = active_item
            while current:
                active_path_ids.add(current.id)
                current = item_map.get(current.parent_id)

    except Menu.DoesNotExist:
        # Если меню с таким именем не найдено, возвращаем пустой контекст
        return {'menu_items': [], 'active_path_ids': set(), 'active_item_id': None}

    # Передаем в контекст шаблона для рекурсивного рендеринга
    return {
        'menu_items': root_items,  # Передаем только корневые элементы, остальное рекурсивно
        'active_path_ids': active_path_ids,
        'active_item_id': active_item.id if active_item else None,
        'request': request
    }
