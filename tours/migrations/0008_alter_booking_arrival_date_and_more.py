# Generated by Django 5.1 on 2024-09-01 17:34

import django.core.validators
import util.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_alter_booking_adults_alter_booking_arrival_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateTimeField(auto_now=True, null=True, validators=[util.model_validators.arrival_date_validator]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(100, 'Name can not be longer than 100 letters'), django.core.validators.MinLengthValidator(2, 'Name can be shorter then two letters'), django.core.validators.RegexValidator(code='invalid_name', message='Name must contain only letters and spaces', regex='^[A-Za-z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_phone',
            field=models.CharField(max_length=10, validators=[util.model_validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(100, 'Name can not be longer than 100 letters'), django.core.validators.MinLengthValidator(2, 'Name can be shorter then two letters'), django.core.validators.RegexValidator(code='invalid_name', message='Name must contain only letters and spaces', regex='^[A-Za-z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(100, 'Name can not be longer than 100 letters'), django.core.validators.MinLengthValidator(2, 'Name can be shorter then two letters'), django.core.validators.RegexValidator(code='invalid_name', message='Name must contain only letters and spaces', regex='^[A-Za-z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='filter',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(100, 'Name can not be longer than 100 letters'), django.core.validators.MinLengthValidator(2, 'Name can be shorter then two letters'), django.core.validators.RegexValidator(code='invalid_name', message='Name must contain only letters and spaces', regex='^[A-Za-z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='tourpackage',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MaxLengthValidator(100, 'Name can not be longer than 100 letters'), django.core.validators.MinLengthValidator(2, 'Name can be shorter then two letters'), django.core.validators.RegexValidator(code='invalid_name', message='Name must contain only letters and spaces', regex='^[A-Za-z\\s]+$')]),
        ),
    ]
