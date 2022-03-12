from django.shortcuts import render
from store.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    products = Product.objects.all().filter(is_available=True, home=True).order_by('create_date')[:8]
    context = {
        'products' : products,
    }
    
    return render(request, 'home.html', context)


def politicadecookies(request):    
    return render(request, 'politicadecookies.html')