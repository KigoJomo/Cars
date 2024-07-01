# Generated by Django 5.0.3 on 2024-04-26 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('yearMfct', models.IntegerField()),
                ('trimlevel', models.IntegerField()),
                ('locallyAvailable', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='path/to/upload/directory/')),
            ],
        ),
    ]
