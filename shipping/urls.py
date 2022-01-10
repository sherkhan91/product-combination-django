from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('api/ingredients', views.IngredientsList.as_view()),
    path('products', views.products, name='products'),
    path('productsoverview', views.productoverview, name='productsoverview'),
    path('badcombinations', views.badcombination, name='badcombinations')
]