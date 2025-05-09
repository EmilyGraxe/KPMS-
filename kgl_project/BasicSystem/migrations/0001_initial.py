# Generated by Django 5.2 on 2025-05-02 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(choices=[('Beans', 'Beans'), ('Maize', 'Maize'), ('Cowpeas', 'Cowpeas'), ('Gnuts', 'Gnuts'), ('Soyabeans', 'Soyabeans')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('supplier', models.CharField(max_length=100)),
                ('supply_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('supplier', models.CharField(blank=True, max_length=100, null=True)),
                ('reason', models.CharField(blank=True, max_length=1000, null=True)),
                ('supply_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_updates', to='BasicSystem.product')),
            ],
        ),
    ]
