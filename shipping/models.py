from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)  # Name of ingredient.
    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)  # Name of product.
    ingredients = models.ManyToManyField('Ingredient', related_name='ingredients')  # Create M2M 
    created = models.DateTimeField(auto_now_add=True)  # Moment on which the object was created.
    modified = models.DateTimeField(auto_now=True)  # Moment on which the object was last changed.
    is_active = models.BooleanField(default=True, )  # False means the object is deactivated or archived or don't ship currently etc.

    def __str__(self) -> str:
        return self.name

    def get_ingredients(self):
        return  list(self.ingredients.values_list('name', flat=True))



class BadCombination(models.Model):
    ingredient_A = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_a')  # The ingredient A or first.
    ingredient_B = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_b')  # The ingredient B or second.
    reason = models.TextField(help_text='Provide reason why given ingredients can not be combined?')  #  Reason for explanation.

    def __str__(self) -> str:
        return ' '.join((str(self.ingredient_A),str(self.ingredient_B)))

    class Meta:
        unique_together = ('ingredient_A', 'ingredient_B') # UniqueConstraint, also new way but this is tested.
