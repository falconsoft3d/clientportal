from store.models import Product
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from config.models import AdminBase

def home(request):
    products = Product.objects.all().filter(is_available=True, home=True).order_by('create_date')[:8]
    context = {
            'products' : products,
        }
    
    # Admin: Revisamos el config si no lo tenemos lo creamos #
    adminbase_count = AdminBase.objects.all().count()
    if adminbase_count == 0:
        admin = AdminBase()
        admin.name = 'clientportal'
        admin.email = 'demo@demo.com'
        admin.phone = '+34000000000'
        admin.street = "Calle 12"
        admin.save()
    # Admin #
    
    
    if (products.count() == 0):
        products = Product.objects.all().filter(is_available=True).order_by('create_date')[:8]
        if (products.count() == 0):
            return render(request, 'new_project.html', context)
        else:
            context = {
            'products' : products,
            }
            return render(request, 'home.html', context)
    else: 
        return render(request, 'home.html', context)


def politicadecookies(request):    
    return render(request, 'politicadecookies.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contacto" 
            body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email_address'], 
                'phone': form.cleaned_data['phone'], 
                'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'mfalcon@falconsolutions.cl', ['mfalcon@falconsolutions.cl']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home")
    form = ContactForm()
    return render(request, "contact.html", {'form':form})


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)