from django.shortcuts import render
from store.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('create_date')[:8]
    # for product in products:
    #     reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    
    context = {
        'products' : products,
    }
    
    return render(request, 'home.html', context)