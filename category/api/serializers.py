from attr import field, fields
from rest_framework.serializers import ModelSerializer
from category.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'description']