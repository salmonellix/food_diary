from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from food_diary_api.models import Meal, Profile, Product, Day


def home(request):

    return render(request, 'base.html')

def diary(request):
    days = Day.objects.all()

    context = {'days': days}
    return render(request, 'diary.html', context)


def day(request, rid):
    day = Day.objects.filter(id= rid)
    meals = Meal.objects.filter(day = day[0])

    context = {
        'day': day,
        'meals': meals
    }

    return render(request, 'day.html', context)

@api_view(['DELETE', 'GET'])
def productDelete(request, id,rid):
    meal = Meal.objects.get(id=id)
    product = Product.objects.get(id=rid)
    meal.products.remove(product)
    day(request, meal.day.id)
    return day(request, meal.day.id)