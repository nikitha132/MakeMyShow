# Generated by Django 4.1.6 on 2023-02-11 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketBooking', '0014_seats_s_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seats',
            old_name='S_no',
            new_name='S_no1',
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='Status',
            new_name='Status1',
        ),
        migrations.AddField(
            model_name='seats',
            name='S_no2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seats',
            name='S_no3',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seats',
            name='S_no4',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seats',
            name='S_no5',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seats',
            name='S_no6',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seats',
            name='Status2',
            field=models.CharField(default='Unbooked', max_length=10),
        ),
        migrations.AddField(
            model_name='seats',
            name='Status3',
            field=models.CharField(default='Unbooked', max_length=10),
        ),
        migrations.AddField(
            model_name='seats',
            name='Status4',
            field=models.CharField(default='Unbooked', max_length=10),
        ),
        migrations.AddField(
            model_name='seats',
            name='Status5',
            field=models.CharField(default='Unbooked', max_length=10),
        ),
        migrations.AddField(
            model_name='seats',
            name='Status6',
            field=models.CharField(default='Unbooked', max_length=10),
        ),
    ]
