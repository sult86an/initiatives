# Generated by Django 2.1.2 on 2018-12-08 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0006_mainstage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainstage',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 3, 43, 8, 240491)),
        ),
    ]
