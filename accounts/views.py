from email import message
from typing import Type
from warnings import catch_warnings
from django.shortcuts import get_object_or_404, render, redirect
from accounts.forms import RegistrationForm, UserForm, UserProfileForm
from .models import Account, UserProfile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
import requests

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    # orders = Order.objects.order_by('created_at').filter(user_id=request.user.id, is_ordered=True)
    # orders_count = orders.count()
    # userprofile = UserProfile.objects.get(user_id = request.user.id)
    # context = {
    #     'orders' : orders,
    #     'orders_count' : orders_count,
    #     'userprofile' : userprofile,
    # }
    
    return render(request, 'accounts/dashboard.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Has iniciado sesion correctamente')
            
            url = request.META.get('HTTP_REFERER')
            
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=')  for x in query.split('&') )
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')
            
            return redirect('dashboard')
        else:
            messages.error(request, 'Las credenciales son incorrecta')
            return redirect('login')
    
    return render(request, 'accounts/login.html')



@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Has salido')
    return redirect('login')


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            
            current_site = get_current_site(request)
            mail_subject = 'Resetear Password'
            body = render_to_string('accounts/reset_password_email.html', {
                "user" : user,
                "domain" : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()
            
            messages.success(request, 'Un email fue enviado a tu bandeja de entrada')
            
            return redirect('login')
        else:
            messages.error(request, 'La cuenta no existe')
            return redirect('forgotpassword')
            
    
    return render(request, 'accounts/forgotpassword.html')



def register(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # demo@demo.cl
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                               email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            
            
            # Generar un record en UserProfile
            profile = UserProfile()
            profile.user_id = user.id
            profile.profile_picture = 'default/default-user.jpeg'
            profile.save()
            
            
            # Envio de Email
            current_site = get_current_site(request)
            mail_subject = 'Por favor activa tu cuenta'
            body = render_to_string('accounts/account_verification_email.html', {
                "user" : user,
                "domain" : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()
            
            
            # messages.success(request, 'Se regitro el usuario exitosamente')
            return redirect("/accounts/login/?command=verification&email="+email)
            
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        user = Account.objects.get(username__exact=request.user.username)
        
        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                
                messages.success(request, 'Su contraseña a cambiado correctamente')
                return redirect('change_password')
            else:
                messages.error(request, 'Por favor ingrese una contraseña valida')
                return redirect('change_password')
        else:
            messages.error(request, 'El password no coicid con el actual')
            return redirect('change_password')
        
    return render(request, 'accounts/change_password.html')
