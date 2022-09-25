# Generated by Django 4.0.7 on 2022-09-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0007_alter_ingredient_carbo_alter_ingredient_cl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='carbo',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='cl',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='energy',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fat',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='iron',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='protien',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sodium',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vA',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vB1',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vB2',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vC',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
    ]
