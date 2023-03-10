# Generated by Django 4.1.1 on 2023-03-05 07:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 7, 4, 14, 579244)),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.CharField(choices=[('py', 'python'), ('cpp', 'C++'), ('js', 'JavaScript')], max_length=30),
        ),
    ]
