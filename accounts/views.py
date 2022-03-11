from email import message
from typing import Type
from warnings import catch_warnings
from django.shortcuts import get_object_or_404, render, redirect

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

@login_required(login_url='/')
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
