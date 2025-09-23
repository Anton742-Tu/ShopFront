from django.shortcuts import render, get_object_or_404

from .models import Contact, Product


def home_page(request):
    """Главная страница - последние 6 товаров"""
    latest_products = Product.objects.order_by('-created_at')[:6]

    # Выводим в консоль
    print("\n" + "=" * 50)
    print("ПОСЛЕДНИЕ 6 ПРОДУКТОВ ДЛЯ ГЛАВНОЙ:")
    for product in latest_products:
        print(f"- {product.name} - {product.price} руб.")
    print("=" * 50 + "\n")

    context = {
        'products': latest_products,
        'page_title': 'Новинки'
    }
    return render(request, 'index.html', context)


def contacts_page(request):
    """Страница контактов"""

    main_contact = Contact.objects.filter(is_main_contact=True, is_active=True).first()

    if main_contact and main_contact.person_name:
        # Режим одного человека
        contacts = Contact.objects.filter(
            person_name=main_contact.person_name,
            is_active=True
        ).order_by('order')
        page_title = main_contact.person_name
        show_person = True
    else:
        # Режим всех контактов
        contacts = Contact.objects.filter(is_active=True).order_by('order')
        page_title = "Наши контакты"
        show_person = False

    context = {
        'contacts': contacts,
        'page_title': page_title,
        'show_person': show_person
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
    """Страница каталога - все товары"""
    all_products = Product.objects.all()

    context = {
        'products': all_products,
        'page_title': 'Все товары',
        'show_filters': True  # Флаг для показа фильтров в шаблоне
    }
    return render(request, 'catalog.html', context)


def category_page(request):
    """Страница категории"""
    return render(request, "category.html")


def product_detail(request, product_id):
    """Страница с подробной информацией о товаре"""
    product = get_object_or_404(Product, id=product_id)

    # Выводим в консоль для отладки
    print(f"\nПросмотр товара: {product.name} (ID: {product.id})")

    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)
