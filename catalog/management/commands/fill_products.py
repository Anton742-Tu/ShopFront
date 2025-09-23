from django.core.management.base import BaseCommand
from django.utils import timezone

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Заполняет базу тестовыми продуктами и категориями (удаляет старые данные)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=10,
            help="Количество продуктов для создания (по умолчанию: 10)",
        )

    def handle(self, *args, **options):
        product_count = options["count"]

        # Удаляем все существующие данные
        self.stdout.write("Удаляем старые данные...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        self.stdout.write("Создаем категории...")
        categories_data = [
            {"name": "Электроника", "description": "Гаджеты и техника"},
            {"name": "Одежда", "description": "Модная одежда и аксессуары"},
            {"name": "Книги", "description": "Художественная и учебная литература"},
            {"name": "Спорт", "description": "Спортивные товары и инвентарь"},
            {"name": "Другое", "description": "Товары без категории"},
        ]

        categories = {}
        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            categories[cat_data["name"]] = category
            self.stdout.write(f"Создана категория: {category.name}")

        # Создаем продукты
        self.stdout.write(f"Создаем {product_count} продуктов...")
        products_data = [
            {
                "name": "iPhone 15 Pro",
                "description": "Флагманский смартфон Apple",
                "price": 99999.99,
                "category": categories["Электроника"],
            },
            {
                "name": "Samsung Galaxy S24",
                "description": "Мощный Android-смартфон",
                "price": 79999.50,
                "category": categories["Электроника"],
            },
            {
                "name": "Футболка хлопковая",
                "description": "Комфортная хлопковая футболка",
                "price": 2499.99,
                "category": categories["Одежда"],
            },
            {
                "name": "Джинсы",
                "description": "Стильные джинсы премиум качества",
                "price": 5999.99,
                "category": categories["Одежда"],
            },
            {
                "name": "Python для начинающих",
                "description": "Учебник по программированию",
                "price": 1899.00,
                "category": categories["Книги"],
            },
            {
                "name": "Война и мир",
                "description": "Классика русской литературы",
                "price": 1299.50,
                "category": categories["Книги"],
            },
            {
                "name": "Беспроводные наушники",
                "description": "Наушники с шумоподавлением",
                "price": 8999.99,
                "category": categories["Электроника"],
            },
            {
                "name": "Фитнес-браслет",
                "description": "Умный браслет для отслеживания активности",
                "price": 3999.50,
                "category": categories["Спорт"],
            },
            {
                "name": "Мяч футбольный",
                "description": "Профессиональный футбольный мяч",
                "price": 2999.99,
                "category": categories["Спорт"],
            },
            {
                "name": "Кружка",
                "description": "Керамическая кружка с принтом",
                "price": 999.99,
                "category": categories["Другое"],
            },
        ]

        # Создаем указанное количество продуктов
        for i in range(min(product_count, len(products_data))):
            prod_data = products_data[i]
            product = Product.objects.create(**prod_data)
            self.stdout.write(f"Создан продукт: {product.name} - {product.price} руб.")

        # Если нужно больше продуктов чем в шаблоне - создаем дополнительные
        if product_count > len(products_data):
            for i in range(len(products_data), product_count):
                product = Product.objects.create(
                    name=f"Товар {i + 1}",
                    description=f"Описание товара {i + 1}",
                    price=1000 + (i * 100),
                    category=categories["Другое"],
                )
                self.stdout.write(
                    f"Создан дополнительный продукт: {product.name} - {product.price} руб."
                )

        # Итог
        self.stdout.write(
            self.style.SUCCESS(
                f"Успешно создано: {Category.objects.count()} категорий и {Product.objects.count()} продуктов!"
            )
        )
