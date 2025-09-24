from django.db import models
from django.utils import timezone


class Category(models.Model):
    """Модель категории товаров"""

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,  # Необязательное поле
        null=True,  # Может быть пустым в БД
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]  # Сортировка по имени

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""

    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите название товара"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="products/",  # Папка для загрузки изображений
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # При удалении категории товар остается
        verbose_name="Категория",
        help_text="Выберите категорию товара",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,  # Максимум 10 цифр
        decimal_places=2,  # 2 знака после запятой
        verbose_name="Цена за покупку",
        help_text="Введите цену товара",
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # Автоматическое обновление при сохранении
        verbose_name="Дата последнего изменения",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at"]  # Новые товары сначала

    def __str__(self):
        return f"{self.name} - {self.price} руб."


class Contact(models.Model):
    CONTACT_TYPES = [
        ("phone", "Телефон"),
        ("email", "Email"),
        ("address", "Адрес"),
        ("whatsapp", "WhatsApp"),
        ("telegram", "Telegram"),
        ("vk", "VK"),
    ]

    # Существующие поля
    contact_type = models.CharField(
        "Тип контакта", max_length=20, choices=CONTACT_TYPES
    )
    value = models.CharField("Значение", max_length=200)
    description = models.TextField(
        "Описание", blank=True, default=""
    )  # ← Добавил default=''
    icon = models.CharField("Иконка", max_length=50, blank=True, default="")
    is_active = models.BooleanField("Активный", default=True)
    order = models.IntegerField("Порядок", default=0)

    # Новые поля
    person_name = models.CharField(
        "Имя человека", max_length=100, blank=True, default=""
    )
    is_main_contact = models.BooleanField(
        "Основной контакт для страницы", default=False
    )

    class Meta:
        ordering = ["-is_main_contact", "order", "contact_type"]
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        if self.person_name:
            return f"{self.person_name} - {self.get_contact_type_display()}"
        return f"{self.get_contact_type_display()} - {self.value}"
