from django.shortcuts import render
from .models import Product, Contact


def home_page(request):
    """Домашняя страница с последними 5 продуктами"""
    # Получаем последние 5 созданных продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим в консоль
    print("\n" + "=" * 50)
    print("ПОСЛЕДНИЕ 5 ПРОДУКТОВ:")
    for product in latest_products:
        print(f"- {product.name} ({product.created_at}) - {product.price} руб.")
    print("=" * 50 + "\n")

    # Передаем в шаблон
    context = {
        'latest_products': latest_products
    }
    return render(request, 'index.html', context)


def contacts_page(request):
    """Страница контактов"""
    # Получаем все контактные данные
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts
    }
    return render(request, 'contacts.html', context)


def handle_form_submission(request):
    """Обработка формы обратной связи"""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print("\n" + "=" * 50)
        print("НОВАЯ ЗАЯВКА С ФОРМЫ:")
        print(f"Имя: {name}")
        print(f"Email: {email}")
        print(f"Сообщение: {message}")
        print("=" * 50 + "\n")

        return render(request, "contacts.html", {"success": True})

    # Если GET-запрос, просто показываем форму
    return render(request, "contacts.html")


def catalog_page(request):
    """Страница каталога"""
    return render(request, "catalog.html")


def category_page(request):
    """Страница категории"""
    return render(request, "category.html")
