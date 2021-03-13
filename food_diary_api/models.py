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
    calories = models.FloatField(default=0,null=True)
    proteins = models.FloatField(default=0,null=True)
    carbs = models.FloatField(default=0,null=True)
    fats = models.FloatField(default=0,null=True)
    amount = models.FloatField(default=0,null=True)

    def __str__(self):
        return self.product_name

    def count_kcal(self):
        return (self.calories* self.amount)/100




class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default='')


    def __str__(self):
        return str(self.date)



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
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal_name

    def get_products(self):
        return self.products

    def count_kcal(self):
        kcals = 0
        p_list = self.products.get()
        for p in list(p_list):
            kcals += p.calories
        return kcals
