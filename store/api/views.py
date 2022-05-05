from ast import Import
from requests import post
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from yaml import serialize
from store.models import Product
from store.api.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class ProductModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()