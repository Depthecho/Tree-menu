from django.shortcuts import render

# Общая функция для рендеринга страницы с именем
def render_menu_page(request, page_name):
    return render(request, 'menu_app/base.html', {'page_name': page_name})

# Представления для различных страниц, использующие общую функцию
def home_page(request):
    return render_menu_page(request, "Главная страница")

def about_page(request):
    return render_menu_page(request, "Страница о нас")

def contacts_page(request):
    return render_menu_page(request, "Страница контактов")

def products_page(request):
    return render_menu_page(request, "Страница продуктов")

def categories_page(request):
    return render_menu_page(request, "Страница категорий продуктов")

def electronics_category_page(request):
    return render_menu_page(request, "Категория: Электроника")

def laptops_page(request):
    return render_menu_page(request, "Раздел: Ноутбуки")

def gaming_laptops_page(request):
    return render_menu_page(request, "Игровые ноутбуки")

def work_laptops_page(request):
    return render_menu_page(request, "Рабочие ноутбуки")

def smartphones_page(request):
    return render_menu_page(request, "Категория: Смартфоны")

def apparel_category_page(request):
    return render_menu_page(request, "Категория: Одежда")

def popular_products_page(request):
    return render_menu_page(request, "Популярные товары")


# Представления для второго меню
def blog_page(request):
    return render_menu_page(request, "Страница блога")

def blog_latest_page(request):
    return render_menu_page(request, "Последние статьи блога")

def blog_archive_page(request):
    return render_menu_page(request, "Архив блога")

def blog_archive_2023_page(request):
    return render_menu_page(request, "Архив блога: 2023")

def blog_archive_2024_page(request):
    return render_menu_page(request, "Архив блога: 2024")

def faq_page(request):
    return render_menu_page(request, "Страница часто задаваемых вопросов")

def help_page(request):
    return render_menu_page(request, "Страница помощи")