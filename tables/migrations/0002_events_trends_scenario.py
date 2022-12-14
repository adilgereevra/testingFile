# Generated by Django 4.1 on 2022-10-14 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('events_id', models.AutoField(primary_key=True, serialize=False)),
                ('events_name', models.CharField(max_length=150, verbose_name='Events')),
                ('trends_file_name', models.CharField(max_length=50, verbose_name='Events file')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trends',
            fields=[
                ('trends_id', models.AutoField(primary_key=True, serialize=False)),
                ('trends_name', models.CharField(max_length=150, verbose_name='Trends')),
                ('trends_file_name', models.CharField(max_length=50, verbose_name='Trends file')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('scenario_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('events_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tables.events')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tables.model2')),
                ('trends_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tables.trends')),
            ],
        ),
    ]
