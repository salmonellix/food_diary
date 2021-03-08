from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from food_diary_api.models import Meal, Profile, Product, Day


def home(request):
    days = Day.objects.all()

    context = {'days': days}
    return render(request, 'index.html', context)


def day(request, rid):
    day = Day.objects.filter(id= rid)
    meals = Meal.objects.filter(day = day[0])

    context = {
        'day': day,
        'meals': meals
    }

    return render(request, 'day.html', context)





