# Generated by Django 5.0.4 on 2024-05-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_car_image_carimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='path/to/upload/directory/'),
        ),
    ]
