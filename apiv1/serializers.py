from attr import field, fields
from rest_framework.serializers import ModelSerializer
from store.models import Product, Color, Size
from category.models import Category

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price']

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'sequence']

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ['name', 'sequence']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'description']