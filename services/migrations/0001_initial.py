# Generated by Django 3.2.4 on 2021-06-15 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wilayas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1500)),
                ('is_validated', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True, verbose_name='adresse')),
                ('longtitude', models.CharField(max_length=20)),
                ('latitude', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=11)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('deleted', models.BooleanField(default=False)),
                ('visibility', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_services', to='categories.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_services', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('wilaya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wilaya_service', to='wilayas.wilaya')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
    ]
