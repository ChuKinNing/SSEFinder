# Generated by Django 3.1.8 on 2021-05-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20210504_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(help_text='Date of the event', null=True),
        ),
        migrations.DeleteModel(
            name='SSE',
        ),
    ]
