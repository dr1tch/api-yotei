# Generated by Django 3.2.4 on 2021-06-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20210630_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start',
            field=models.TimeField(),
        ),
    ]
