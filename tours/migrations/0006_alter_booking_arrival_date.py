# Generated by Django 5.1 on 2024-08-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_category_created_at_category_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
