# Generated by Django 2.1.2 on 2018-12-08 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0007_auto_20181208_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainstage',
            name='ratio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mainstage',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 11, 3, 21, 761555)),
        ),
    ]
