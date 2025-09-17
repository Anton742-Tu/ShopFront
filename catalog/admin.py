from django.contrib import admin
from .models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Отображаем id и name в списке
    list_display_links = ('name',)  # Делаем имя кликабельным
    search_fields = ('name', 'description')  # Поиск по name и description


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Отображаем id, name, price, category
    list_display_links = ('name',)  # Делаем имя кликабельным
    list_filter = ('category',)  # Фильтрация по категории
    search_fields = ('name', 'description')  # Поиск по name и description
    readonly_fields = ('created_at', 'updated_at')  # Только для чтения

    # Группировка полей в форме редактирования
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'category', 'price')
        }),
        ('Изображение', {
            'fields': ('image',),
            'classes': ('collapse',)  # Сворачиваемый блок
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_type', 'value', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('contact_type', 'is_active')
    search_fields = ('value', 'description')
