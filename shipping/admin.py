from django.contrib import admin
from shipping.models import Ingredient, Product, BadCombination

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_ingredients')  # Custom property to view product ingredients.
    search_fields = ('name',)



class BadCombinationAdmin(admin.ModelAdmin):
    list_display = ('ingredient_A', 'ingredient_B')
    search_fields = ('ingredient_A__name','ingredient_B__name')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BadCombination, BadCombinationAdmin)
