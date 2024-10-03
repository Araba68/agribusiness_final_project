# Generated by Django 5.1.1 on 2024-09-27 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_quantity', models.PositiveIntegerField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.farmer')),
            ],
        ),
    ]
