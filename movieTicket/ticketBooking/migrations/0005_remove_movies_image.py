# Generated by Django 4.1.6 on 2023-02-09 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketBooking', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='image',
        ),
    ]