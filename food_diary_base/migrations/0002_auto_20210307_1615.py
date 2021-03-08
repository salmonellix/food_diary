# Generated by Django 3.1.7 on 2021-03-07 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_diary_base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='meals',
        ),
        migrations.AddField(
            model_name='meal',
            name='day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='food_diary_base.day'),
            preserve_default=False,
        ),
    ]