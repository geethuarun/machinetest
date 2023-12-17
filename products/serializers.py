from rest_framework import serializers
from products.models import Category,Product


class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    

    class Meta:
        model=Category
        fields=["id","category_name"]

class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    category_name=serializers.CharField(read_only=True)
    class Meta:
        model=Product
        fields="__all__"

        # def create(self, validated_data):
        # return Product.objects.create_user(**validated_data)
    