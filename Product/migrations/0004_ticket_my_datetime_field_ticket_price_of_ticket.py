# Generated by Django 5.0 on 2024-05-17 17:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_ticket_prize_categories_alter_ticket_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='my_datetime_field',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ticket',
            name='price_of_ticket',
            field=models.CharField(default=0),
        ),
    ]
