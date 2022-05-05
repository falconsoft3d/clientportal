from rest_framework.viewsets import ViewSet, ModelViewSet
from store.models import Product, Color, Size
from category.models import Category
from apiv1.serializers import ProductSerializer, ColorSerializer, SizeSerializer, CategorySerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class ProductModeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ColorModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ColorSerializer
    queryset = Color.objects.all()

class SizeModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SizeSerializer
    queryset = Size.objects.all()

class CategoryModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()