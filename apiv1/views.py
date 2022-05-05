from rest_framework.viewsets import ViewSet, ModelViewSet
from store.models import Product, Color, Size
from apiv1.serializers import ProductSerializer, ColorSerializer, SizeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class ProductModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
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