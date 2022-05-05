from rest_framework.viewsets import ModelViewSet
from accounts.models import Account
from store.models import Product, Color, Size, AccountPrice
from category.models import Category
from orders.models import Order
from apiv1.serializers import ProductSerializer, ColorSerializer, SizeSerializer, CategorySerializer, \
    AccountSerializer, AccountPriceSerializer, OrderSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class OrderModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class AccountPriceModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = AccountPriceSerializer
    queryset = AccountPrice.objects.all()

class AccountModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class ProductModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser,IsAuthenticatedOrReadOnly]
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