# Generated by Django 5.0 on 2024-05-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0003_remove_useraccountmodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('deposit', 'DEPOSIT'), ('withdrawal', 'WITHDRAWAL')], max_length=10),
        ),
        migrations.AlterField(
            model_name='useraccountmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]