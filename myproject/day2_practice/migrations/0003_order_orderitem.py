# Generated by Django 5.1.4 on 2025-01-09 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day2_practice', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('order_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='day2_practice.order')),
            ],
        ),
    ]
