# Generated by Django 3.1.7 on 2021-03-08 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('calories', models.FloatField(default=0, null=True)),
                ('proteins', models.FloatField(default=0, null=True)),
                ('carbs', models.FloatField(default=0, null=True)),
                ('fats', models.FloatField(default=0, null=True)),
                ('amount', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(choices=[('BREAKFAST', 'breakfast'), ('SNACK I', 'snack I'), ('LUNCH', 'lunch'), ('SNACK II', 'snack II'), ('SNACK III', 'snack III'), ('DINER', 'diner'), ('SNACK IV', 'snack IV')], max_length=100)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_diary_api.day')),
                ('products', models.ManyToManyField(blank=True, default='', to='food_diary_api.Product')),
            ],
        ),
    ]