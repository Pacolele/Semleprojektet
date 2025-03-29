# Generated by Django 5.1.7 on 2025-03-29 09:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semlerating', '0002_rating_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='user_agent',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
