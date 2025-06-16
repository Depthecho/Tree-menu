from django.contrib import admin
from .models import Menu, MenuItem

# Регистрация модели Menu в админке
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Регистрация модели MenuItem в админке
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'url', 'named_url',)
    list_filter = ('menu',)
    search_fields = ('title', 'url', 'named_url',)

    raw_id_fields = ('parent',)
