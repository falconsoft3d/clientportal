from attr import field, fields
from rest_framework.serializers import ModelSerializer
from store.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price']
        # fields = '__all__'