# Generated by Django 2.1.2 on 2018-12-08 15:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0009_auto_20181208_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainstage',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 18, 58, 55, 871004)),
        ),
        migrations.AlterField(
            model_name='mainstage',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='initiatives.Stages'),
        ),
    ]
