from django.contrib import admin
from .models import Profile, Day, Meal, Product


admin.site.register(Product)
admin.site.register(Meal)
admin.site.register(Day)
admin.site.register(Profile)