
from dataclasses import fields
from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)


class CollectionDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'collection', 'price_with_tax',
                  'collection', 'collection_details']
    price_with_tax = serializers.SerializerMethodField(
        method_name='get_price_with_tax')

    collection = CollectionSerializer()
    collection_details = serializers.HyperlinkedRelatedField(
        view_name='collection-detail', queryset=Collection.objects.all(), source='collection')

    def get_price_with_tax(self, product: Product):
        return Decimal(product.price * Decimal(1.1))
