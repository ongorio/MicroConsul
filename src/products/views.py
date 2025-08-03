from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.services import ProductsService

class ProductsApi(APIView):
    def get(self, request):
        products = ProductsService.get_products()
        return Response(products, status=status.HTTP_200_OK)

class ProductApi(APIView):
    def get(self, request, id):
        product = ProductsService.get_product_by_id(id)
        
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(product, status=status.HTTP_200_OK)