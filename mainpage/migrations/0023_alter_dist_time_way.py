# Generated by Django 5.1.3 on 2025-01-12 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0022_alter_dist_time_way'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dist',
            name='time_way',
            field=models.DateField(verbose_name=datetime.datetime(2025, 1, 12, 13, 11, 34, 527102)),
        ),
    ]
