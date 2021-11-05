# Generated by Django 3.2.4 on 2021-07-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_service_agents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='service',
            name='longtitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]