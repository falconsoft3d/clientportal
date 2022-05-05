from rest_framework.viewsets import ViewSet, ModelViewSet
from category.models import Category
from category.api.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class CategoryModeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()