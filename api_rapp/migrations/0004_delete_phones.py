# Generated by Django 4.0.6 on 2022-08-25 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rapp', '0003_alter_phones_id_dt'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Phones',
        ),
    ]