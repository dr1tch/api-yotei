# Generated by Django 3.2.4 on 2021-07-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_service_wilaya'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='agents',
            field=models.IntegerField(default=1),
        ),
    ]