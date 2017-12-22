# Generated by Django 2.0 on 2017-12-15 20:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171215_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2017, 12, 15, 20, 14, 48, 406063, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
