from rest_framework import serializers 
from storeapp.models import Product , Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        # fields= '__all__'
        fields =['id','name','description','category','slug','inventory','old_price','price']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ['category_id','title','slug']