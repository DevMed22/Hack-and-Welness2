# Generated by Django 4.0.7 on 2022-09-24 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0004_alter_ingredient_carbo_alter_ingredient_cl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='vB',
        ),
    ]