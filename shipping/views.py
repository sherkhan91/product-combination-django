from django.http.response import HttpResponse, JsonResponse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from shipping.models import Ingredient, Product, BadCombination
from shipping.serializers import BadCombinationSerializer, ProductOverviewSerializer, ProductSerializer, IngredientSerializer
from rest_framework import status
from rest_framework import mixins, generics

# Create your views here.

def index(request):
    return HttpResponse('Hello, Welcome to the Chemi Delivery, Shipping site.')

@api_view(['GET'])
def ingredients(request):
    """
    this view will return all ingredients
    """
    all_ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(all_ingredients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def products(request):
    if request.method == 'GET':
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def productoverview(request):
    all_products = Product.objects.all()
    serializer = ProductOverviewSerializer(all_products, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def badcombination(request):
    if request.method == 'GET':
        blocked_combinations = BadCombination.objects.all()
        serializer = BadCombinationSerializer(blocked_combinations, many=True)
        return Response(serializer.data)
