from store.models import Product
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def home(request):
    products = Product.objects.all().filter(is_available=True, home=True).order_by('create_date')[:8]
    context = {
        'products' : products,
    }
    
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