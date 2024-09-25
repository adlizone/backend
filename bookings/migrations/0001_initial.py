# Generated by Django 5.1 on 2024-09-25 03:53

import django.core.validators
import django.db.models.deletion
import util.model_validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tours', '0011_alter_booking_children'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_adults', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, 'Enter a value in the range 1-30'), django.core.validators.MaxValueValidator(30, 'Enter a value in the range 1-30')])),
                ('number_of_children', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, 'Enter a value in the range 0-30'), django.core.validators.MaxValueValidator(30, 'Enter a value in the range 0-30')])),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('arrival_date', models.DateField(auto_now=True, null=True, validators=[util.model_validators.arrival_date_validator])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('tour_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tourpackage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(max_length=255, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='created', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='bookings.booking')),
            ],
        ),
    ]
