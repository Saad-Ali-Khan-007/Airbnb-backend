# Generated by Django 5.0.2 on 2024-06-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(null=True),
        ),
    ]
