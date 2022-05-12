from distutils.command.upload import upload
from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count
from accounts.get_username import get_username


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50, unique=True)
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.FloatField(default=1)
    images = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=13, default="-")
    home = models.BooleanField(default=False)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, null=True, blank=True)
    size = models.ForeignKey(
        Size, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.IntegerField(default=0)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    @property
    def is_a_variant(self):
        return self.parent is not None

    @property
    def variants(self):
        return Product.objects.filter(parent=self.id)

    @property
    def tablevariants(self):
        variants = Product.objects.filter(parent=self.id)
        tablearray = []
        counter = 0
        for variant in variants:
            color = 0
            size = 0
            stock = 0
            # Llenamos el Color
            if variant.color:
                color = variant.color.id

            # Llenamos el Tamaño
            if variant.size:
                size = variant.size.id

            price = variant.price

            tablearray.append([color,size,variant.stock,price])
        return tablearray

    @property
    def has_variants(self):
        return self.variants.count() > 0

    @property
    def is_parent(self):
        return not self.is_a_variant and self.has_variants

    def position(self, sizes: list, colors: list) -> tuple:
        return (
            sizes.index(self.size.id),
            colors.index(self.color.id)
        )

    def __str__(self):
        if not self.is_a_variant:
            return self.product_name

        return f'Color: {self.color.name}, Size: {self.size.name}'

    def get_list_price(product, user):
        product_obj = Product.objects.get(id=product)
        price = product_obj.price
        try:
            account_price = AccountPrice.objects.get(
                product=product_obj.id, account=user)
            if account_price:
                price = account_price.listprice
        except Exception as e:
            pass
        return price


class ProductGallery(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.product_name


class AccountPrice(models.Model):
    account = models.ForeignKey(
        Account, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    listprice = models.FloatField(default=1)

    def __str__(self):
        return self.product.product_name


class AccountFavorite(models.Model):
    account = models.ForeignKey(
        Account, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.product_name
