from django.db import models
from django.utils import timezone


class Category(models.Model):
    """Модель категории товаров"""
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите название категории'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание категории',
        blank=True,  # Необязательное поле
        null=True  # Может быть пустым в БД
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']  # Сортировка по имени

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите название товара'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание товара',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='products/',  # Папка для загрузки изображений
        verbose_name='Изображение',
        help_text='Загрузите изображение товара',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # При удалении категории товар остается
        verbose_name='Категория',
        help_text='Выберите категорию товара',
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,  # Максимум 10 цифр
        decimal_places=2,  # 2 знака после запятой
        verbose_name='Цена за покупку',
        help_text='Введите цену товара'
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # Автоматическое обновление при сохранении
        verbose_name='Дата последнего изменения'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']  # Новые товары сначала

    def __str__(self):
        return f"{self.name} - {self.price} руб."


class Contact(models.Model):
    """Модель для хранения контактных данных"""

    # Типы контактов
    CONTACT_TYPES = [
        ('phone', 'Телефон'),
        ('email', 'Email'),
        ('address', 'Адрес'),
        ('schedule', 'Режим работы'),
        ('other', 'Другое'),
    ]

    contact_type = models.CharField(
        max_length=20,
        choices=CONTACT_TYPES,
        verbose_name='Тип контакта',
        help_text='Выберите тип контактной информации'
    )
    value = models.CharField(
        max_length=200,
        verbose_name='Значение',
        help_text='Например: +7 (999) 123-45-67 или info@example.com'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
        help_text='Дополнительное описание (необязательно)'
    )
    icon = models.CharField(
        max_length=50,
        verbose_name='Иконка',
        blank=True,
        null=True,
        help_text='Класс иконки Bootstrap Icons (например: bi-telephone)'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения',
        help_text='Чем меньше число, тем выше в списке'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Показывать на сайте'
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.get_contact_type_display()}: {self.value}"
