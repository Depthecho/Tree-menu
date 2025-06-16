from django.db import models
from django.urls import reverse, NoReverseMatch


# Модель для представления отдельного меню
class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название меню")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name


# Модель для представления отдельного пункта меню
class MenuItem(models.Model):
    # Связь с моделью Menu: каждый пункт принадлежит определенному меню
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name="Меню")

    # Название пункта меню
    title = models.CharField(max_length=255, verbose_name="Название пункта")

    # Явный URL-адрес
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Явный URL")

    # Именованный URL-адрес Django
    named_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Именованный URL")

    # Связь с самим собой для создания древовидной структуры (родительский пункт)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Родительский пункт"
    )

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return f"{self.title} ({self.menu.name})"

    # Метод для получения абсолютного URL для данного пункта меню
    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                # Если named_url не может быть разрешен, возвращаем заглушку
                return "#invalid_named_url"
        return "#"  # Если ни явный, ни именованный URL не заданы
