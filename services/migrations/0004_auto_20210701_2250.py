# Generated by Django 3.2.4 on 2021-07-01 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wilayas', '0001_initial'),
        ('services', '0003_alter_service_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'service', 'verbose_name_plural': 'services'},
        ),
        migrations.AlterField(
            model_name='service',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wilaya_services', to='wilayas.wilaya'),
        ),
    ]
