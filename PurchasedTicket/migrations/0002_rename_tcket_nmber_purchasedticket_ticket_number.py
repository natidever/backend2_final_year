# Generated by Django 5.0 on 2024-05-17 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PurchasedTicket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasedticket',
            old_name='Tcket_nmber',
            new_name='Ticket_number',
        ),
    ]
