from email import message
from django.shortcuts import get_object_or_404, render, redirect
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Product

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None :
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by('-create_date')
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-create_date')
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
        product_count = products.count()
    
    context = {
        'products' : paged_products,
        'product_count' : product_count
    }
    
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug)
        # in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        
    except Exception as e:
        raise e
    
    # if request.user.is_authenticated:
    #     try:
    #         orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
    #     except OrderProduct.DoesNotExist:
    #         orderproduct = None
    # else:
    #      orderproduct = None
        
        
    # reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)
    # product_gallery = ProductGallery.objects.filter(product_id=single_product.id)
    
    context = {
        'single_product' : single_product,
    }
    
    return render(request, 'store/product_detail.html', context)