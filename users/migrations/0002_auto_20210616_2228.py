# Generated by Django 3.2.4 on 2021-06-16 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]