# Generated by Django 5.2 on 2025-05-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_remove_sale_customer_name_remove_sale_nin'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
