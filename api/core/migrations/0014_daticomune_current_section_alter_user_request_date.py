# Generated by Django 4.1.2 on 2023-01-19 22:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_daticomune_cont_commessa_anno1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='daticomune',
            name='current_section',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 23, 3, 27, 624353)),
        ),
    ]
