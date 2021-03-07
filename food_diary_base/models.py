from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Q

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(default='')


    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    calories = models.IntegerField(default=0)
    proteins = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    fats = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Meal(models.Model):
    # list of meals to choose
    MEALS = (
        ('BREAKFAST', 'breakfast'),
        ('SNACK I', 'snack I'),
        ('LUNCH', 'lunch'),
        ('SNACK II', 'snack II'),
        ('SNACK III', 'snack III'),
        ('DINER', 'diner'),
        ('SNACK IV', 'snack IV')
    )
    meal_name = models.CharField(max_length=100, choices=MEALS)
    products = models.ManyToManyField(Product, blank=True, default='')
    #day = models.oreignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal_name

    def get_products(self):
        return self.products


class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default='')
    meals = models.ManyToManyField(Meal, blank=True, default='')


    def __str__(self):
        return str(self.date)

    def get_meals(self):
        return self.meals
