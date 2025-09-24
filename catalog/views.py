from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Contact, Product


def add_product(request):
    """Страница добавления нового товара"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Товар "{product.name}" успешно добавлен!')
            return redirect('product_detail', pk=product.id)
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ProductForm()

    context = {
        'form': form,
        'page_title': 'Добавить товар'
    }
    return render(request, 'catalog/add_product.html', context)


def home_page(request):
    """Главная страница с пагинацией"""
    # Получаем все товары (или можно оставить только последние)
    all_products = Product.objects.order_by("-created_at")

    # Настраиваем пагинацию - 6 товаров на страницу
    paginator = Paginator(all_products, 6)
    page_number = request.GET.get("page", 1)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {"products": products, "page_title": "Новинки"}
    return render(request, "index.html", context)


def contacts_page(request):
    """Страница контактов"""

    main_contact = Contact.objects.filter(is_main_contact=True, is_active=True).first()

    if main_contact and main_contact.person_name:
        # Режим одного человека
        contacts = Contact.objects.filter(
            person_name=main_contact.person_name, is_active=True
        ).order_by("order")
        page_title = main_contact.person_name
        show_person = True
    else:
        # Режим всех контактов
        contacts = Contact.objects.filter(is_active=True).order_by("order")
        page_title = "Наши контакты"
        show_person = False

    context = {
        "contacts": contacts,
        "page_title": page_title,
        "show_person": show_person,
    }
    return render(request, "contacts.html", context)


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
    """Страница каталога - все товары с пагинацией"""
    all_products = Product.objects.all()

    # Пагинация - 8 товаров на страницу
    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page', 1)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'page_title': 'Каталог товаров'
    }
    return render(request, 'catalog.html', context)


def category_page(request):
    """Страница категории"""
    return render(request, "category.html")


def product_detail(request, pk=None, product_id=None):
    """Страница с подробной информацией о товаре"""
    # Определяем ID товара
    product_id = product_id or pk

    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)
