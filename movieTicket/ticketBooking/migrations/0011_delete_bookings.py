# Generated by Django 4.1.6 on 2023-02-11 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketBooking', '0010_merge_20230211_1042'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]
