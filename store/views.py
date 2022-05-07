from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from store.serializers import CollectionDetailsSerializer, ProductSerializer
from .models import Collection, Product

# Create your views here.


@api_view()
def product_list(request):
    products_query = Product.objects.select_related('collection').all()[:100]
    products = ProductSerializer(
        products_query, many=True, context={'request': request})
    return Response(products.data)


@api_view()
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    product_serializer = ProductSerializer(
        product, context={'request': request})
    return Response(product_serializer.data)


@api_view()
def colection_details(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    collection_serializer = CollectionDetailsSerializer(
        collection, context={'request': request})
    return Response(collection_serializer.data)
