from rest_framework import serializers
from .models import Categories, Subcategories, Product


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class SubCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
