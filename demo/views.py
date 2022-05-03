from random import random
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product, Category
import requests
import random


def generate_demo_data(request):
    products = Product.objects.all().filter(is_available=True, home=True)

    if (products.count() == 0):
        url = "https://fakestoreapi.com/products"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        json = response.json()

        # Creamos las categorias
        category_obj = Category.objects.filter(category_name="demo")
        if category_obj.count() <= 0:
            category = Category()
            category.category_name = "demo"
            category.description = "demo"
            category.slug = "demo"
            category.save()
        else:
            category = category_obj.first()

        i = 0
        for item in json:
            i += 1
            product = Product()
            product.product_name = item["title"]
            product.price = item["price"]
            product.slug = i
            product.description = item["description"]
            product.code = item["id"]
            product.stock = i * 100
            product.category = category

            product.save()

        return redirect('store')
    else:
        return redirect('store')
