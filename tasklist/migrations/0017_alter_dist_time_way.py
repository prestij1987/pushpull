# Generated by Django 5.1.3 on 2024-11-17 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0016_alter_dist_time_way'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dist',
            name='time_way',
            field=models.DateField(verbose_name=datetime.datetime(2024, 11, 17, 9, 43, 23, 429653)),
        ),
    ]
