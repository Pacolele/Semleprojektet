# Generated by Django 5.1.7 on 2025-03-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semlerating', '0003_alter_semlor_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semlor',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
