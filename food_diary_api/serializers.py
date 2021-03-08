from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Meal, Profile, Product, Day



class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(
#         max_length=100,
#         style={'placeholder': 'Email', 'autofocus': True}
#     )
#     password = serializers.CharField(
#         max_length=100,
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )
#     remember_me = serializers.BooleanField()
