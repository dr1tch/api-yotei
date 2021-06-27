# Generated by Django 3.2.4 on 2021-06-21 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_alter_service_logo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('status', models.IntegerField(choices=[(2, 'Approuved'), (1, 'Pending'), (0, 'Rejected')], default=1, verbose_name='Status')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_client', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_service', to='services.service')),
            ],
            options={
                'verbose_name': 'appointment',
                'verbose_name_plural': 'appointments',
            },
        ),
    ]
