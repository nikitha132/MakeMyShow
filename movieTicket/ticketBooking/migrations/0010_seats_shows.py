# Generated by Django 4.1.6 on 2023-02-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketBooking', '0009_rename_movie_name_bookings_movie_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_No', models.IntegerField()),
                ('Status', models.CharField(default='Unbooked', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='shows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Show_time', models.TimeField()),
            ],
        ),
    ]
