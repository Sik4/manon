# Generated by Django 2.2.1 on 2019-05-23 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 15, 12, 52, 186370), verbose_name='date published'),
        ),
    ]
