# Generated by Django 5.0.4 on 2024-05-06 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_car_currentlocation_car_drivetype_car_enginesize_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
            ],
        ),
    ]
