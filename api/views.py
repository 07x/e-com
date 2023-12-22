from django.shortcuts import render
from storeapp.models import Product,Category
from .serializers import ProductSerializer, CategorySerializer

# DRF 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics 




# # Generes Mixines 
class APIProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class APIProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





# class APIProductList(APIView):
#     def get(self,request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



class APIProduct(APIView):
    def get(self,request,pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
    def put(self,request,pk):
        product = get_object_or_404(Product,id=pk)
        serialier = ProductSerializer(product,data=serialier.data)
        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data)
        else:
            return Response(serialier.errors)

    def delete(self,request,pk):
        product = get_object_or_404(Product, id=pk)
        try:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)



class APICategoryList(APIView):
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class APICategory(APIView):
    def get(self,request,pk):
        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
        
    def put(self,request,pk):
        category = get_object_or_404(Category,category_id=pk)
        serialier = CategorySerializer(category,data=serialier.data)
        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data)
        else:
            return Response(serialier.errors)

    def delete(self,request,pk):
        category = get_object_or_404(Category, category_id=pk)
        try:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
