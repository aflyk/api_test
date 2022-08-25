# Generated by Django 4.0.6 on 2022-08-25 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('entity_id', models.CharField(max_length=255)),
                ('snils', models.CharField(blank=True, max_length=20)),
                ('oiv_id', models.IntegerField()),
                ('theme_id', models.BigIntegerField()),
                ('request_id', models.IntegerField()),
                ('id_dt', models.DateTimeField(default=datetime.datetime.now())),
                ('visit_date', models.DateField()),
            ],
        ),
    ]