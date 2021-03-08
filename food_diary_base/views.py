from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import *


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
