from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Что показывать в списке
    search_fields = ('name', 'description')  # Поиск по этим полям

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')  # Поля в списке
    list_filter = ('category', 'created_at')  # Фильтры справа
    search_fields = ('name', 'description')  # Поиск
    readonly_fields = ('created_at', 'updated_at')  # Только для чтения
