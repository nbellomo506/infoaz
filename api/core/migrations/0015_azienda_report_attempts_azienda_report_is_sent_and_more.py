# Generated by Django 4.1.2 on 2023-01-20 11:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_daticomune_current_section_alter_user_request_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='azienda',
            name='report_attempts',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='azienda',
            name='report_is_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 12, 56, 13, 29055)),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(default=datetime.datetime(2023, 1, 20, 12, 56, 13, 32056))),
                ('azienda', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.azienda')),
                ('user_sent_id', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
