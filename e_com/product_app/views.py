from __future__ import unicode_literals
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Categories, Subcategories, Product
from .serializers import CatSerializer, SubCatSerializer, ProductSerializer


class CategoryList(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CatSerializer


class SubCategoryList(ListAPIView):
    serializer_class = SubCatSerializer

    def get_queryset(self):
        return Subcategories.objects.filter(category=self.kwargs["pk"])


class ProductListFromCategory(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(sub_category__category=self.kwargs['pk'])


class ProductListFromSubCategory(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(sub_category__pk=self.kwargs['pk'])


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
