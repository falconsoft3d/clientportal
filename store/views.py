from email import message
from django.shortcuts import get_object_or_404, render, redirect
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Product, ProductGallery, AccountFavorite
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def store(request, category_slug=None):
    categories = None
    products = None
    product_by_page = 9
    
    # Si mostramos los Favoritos
    if (request.get_full_path() == '/store/favorites/'):
        current_user = request.user
        # Buscamos los productos favoritos para este usuario
        favorites_products = AccountFavorite.objects.filter(account=current_user)
        print("Filtramos por favorito")
        print(favorites_products)
        
        # PENDIENTE
        products = Product.objects.filter(is_available=True).order_by('-create_date')
        
        # Paginamos
        paginator = Paginator(products, product_by_page)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    
    else:
        if category_slug != None :
            categories = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=categories, is_available=True).order_by('-create_date')
            paginator = Paginator(products, product_by_page)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
            product_count = products.count()
        else:
            products = Product.objects.all().filter(is_available=True).order_by('-create_date')
            paginator = Paginator(products, product_by_page)
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
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)
    
    context = {
        'single_product' : single_product,
        'product_gallery' : product_gallery,
    }
    
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-create_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword) )
            product_count = products.count()
        
        context = {
            'products' : products,
            'product_count' : product_count
        }
        
        return render(request, 'store/store.html', context)

@login_required
def add_favorites(request, id):
    
    product = Product.objects.get(id=id)
    current_user = request.user
    account_favorite = AccountFavorite()
    account_favorite.account = current_user
    account_favorite.product = product
    account_favorite.save()
    
    return redirect('favorites_products')