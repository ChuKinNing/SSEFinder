# Generated by Django 3.1.8 on 2021-05-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['location', 'date']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_name',
        ),
        migrations.AddField(
            model_name='case',
            name='date_of_birth',
            field=models.DateField(help_text='Enter the date of birth of the patient', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(help_text='Enter the location', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='venue_location',
            field=models.CharField(help_text='Enter the location', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='HKID',
            field=models.CharField(help_text='Enter Identity Document Number of the case (e.g. A123456(7) )', max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_id',
            field=models.IntegerField(default=0, help_text='Unique ID of the case', unique=True),
        ),
    ]
