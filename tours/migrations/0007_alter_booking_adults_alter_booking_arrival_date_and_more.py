# Generated by Django 5.1 on 2024-08-29 17:21

import django.core.validators
import util.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_alter_booking_arrival_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, 'Enter a value in the range 1-30'), django.core.validators.MaxValueValidator(30, 'Enter a value in the range 1-30')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateTimeField(auto_now=True, null=True, validators=[util.validators.arrival_date_validator]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='children',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, 'Enter a value in the range 0-30'), django.core.validators.MaxValueValidator(30, 'Enter a value in the range 0-30')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Name can not be shorter than two letters')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_phone',
            field=models.CharField(max_length=10, validators=[util.validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Name can not be shorter than two letters')]),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(300, 'Too long description')]),
        ),
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Name can not be shorter than two letters')]),
        ),
        migrations.AlterField(
            model_name='filter',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Name can not be shorter than two letters')]),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='day_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(30, 'Range is 1-30'), django.core.validators.MinValueValidator(1, 'Range is 1-30')]),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='description',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(1000, 'Too long description')]),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Title can not be shorter than two letters')]),
        ),
        migrations.AlterField(
            model_name='tourpackage',
            name='description',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(500, 'Too long description')]),
        ),
        migrations.AlterField(
            model_name='tourpackage',
            name='duration',
            field=models.IntegerField(blank=True, help_text='Duration in days', null=True, validators=[django.core.validators.MaxValueValidator(30, 'Range is 1-30'), django.core.validators.MinValueValidator(1, 'Range is 1-30')]),
        ),
        migrations.AlterField(
            model_name='tourpackage',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(2, 'Name can not be shorter than two letters')]),
        ),
        migrations.AlterField(
            model_name='tourpackage',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.DecimalValidator(10, 2)]),
        ),
    ]
