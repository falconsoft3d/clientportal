from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from store.views import add_favorites

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    
    return redirect('cart')

def remove_cart_item(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart= cart, id=cart_item_id)
    
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    current_user = request.user

    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)

        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            cart_item.list_price = Product.get_list_price(cart_item.product.id, current_user.id)
            cart_item.subtotal = cart_item.list_price * cart_item.quantity
            total += (cart_item.list_price * cart_item.quantity)
            quantity += cart_item.quantity
            
        tax = (21*total)/100
        grand_total = total + tax
    
    except ObjectDoesNotExist:
        pass # Solo ignora
    
    Round = lambda x, n: eval('"%.'+str(int(n))+'f" % '+repr(int(x)+round(float('.'+str(float(x)).split('.')[1]),n)))

    print("cart_items")
    print(cart_items)

    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        'tax' : tax,
        'grand_total' : Round(grand_total, 2)
        
    }
    return render(request, 'store/cart.html', context)


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    current_user = request.user
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
        cart_id = _cart_id(request)
        )
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
            user = current_user
        )
        cart_item.save()
    return redirect('cart')


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    current_user = request.user
    tax = 0
    grand_total = 0
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            cart_item.list_price = Product.get_list_price(cart_item.product.id, current_user.id)
            cart_item.subtotal = cart_item.list_price * cart_item.quantity
            total += (cart_item.list_price * cart_item.quantity)
            quantity += cart_item.quantity
            
        tax = (21*total)/100
        grand_total = total + tax
    
    except ObjectDoesNotExist:
        pass # Solo ignora
    
    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        'tax' : tax,
        'grand_total' : grand_total,
        'userprofile' : userprofile
        
    }
    return render(request, 'orders/checkout.html', context)

@login_required
def clear_cart(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart.delete()
    return redirect('cart')


@login_required
def cart_to_favorite(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    for item in cart_items:
        add_favorites(request, item.product.id)
    return redirect('favorites_products')
    
    
    
    
    
        
        


