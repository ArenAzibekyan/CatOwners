# Generated by Django 2.0 on 2017-12-15 19:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2017, 12, 15, 19, 52, 24, 512195, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
