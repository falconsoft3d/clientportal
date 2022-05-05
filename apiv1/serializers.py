from rest_framework.serializers import ModelSerializer
from store.models import Product, Color, Size, AccountPrice
from category.models import Category
from accounts.models import Account
from orders.models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_number','id']

class AccountPriceSerializer(ModelSerializer):
    class Meta:
        model = AccountPrice
        fields = ['listprice']

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','username', 'email', 'phone_number']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name', 'description', 'price']

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = ['id','name', 'sequence']

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ['id','name', 'sequence']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name', 'description']