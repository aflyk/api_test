# Generated by Django 4.0.6 on 2022-08-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rapp', '0006_alter_phones_id_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='call_duration_category',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='phones',
            name='entity_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='id_dt',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='phones',
            name='oiv_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='phones',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='phones',
            name='request_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='phones',
            name='theme_id',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='phones',
            name='visit_date',
            field=models.DateField(blank=True),
        ),
    ]
