# Generated by Django 5.1.6 on 2025-03-03 19:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0002_remove_sale_sale_price_remove_sale_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='transaction_id',
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
    ]
