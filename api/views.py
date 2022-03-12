from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from store.models import Product
from accounts.models import UserProfile
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class ApiView(View):    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get(self, request, id=0, token=""):
        token = list(UserProfile.objects.filter(token=token).values())
        if len(token) > 0 :
            if(id>0):
                products = list(Product.objects.filter(id=id).values())
                if len(products) > 0 :
                    product = products[0]
                    datos = {'message': "Success", "product": product}
                else:
                    datos = {'result': 'error', 'message': "No se encuentran productos..."}
                return JsonResponse(datos)
            else:
                products = list(Product.objects.values())
                if len(products) > 0 :
                    datos = {'message': "Success", "products": products}
                else:
                    datos = {'result': 'error', 'message': "No se encuentran productos..."}
                return JsonResponse(datos)
        else:
            datos = {'result': 'error', 'message': "Token Incorrecto."}
            return JsonResponse(datos)
