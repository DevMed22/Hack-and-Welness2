# Generated by Django 4.0.7 on 2022-09-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
