from shipping.models import Ingredient, Product, BadCombination
from rest_framework import serializers

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'ingredients')

class ProductOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth = 1
        fields = ('id','name', 'ingredients')


class BadCombinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadCombination
        fields = ('id','ingredient_A','ingredient_B','reason')