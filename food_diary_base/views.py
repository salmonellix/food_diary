from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
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

    return render(request, 'index.html', context)





