# Generated by Django 4.1.7 on 2023-03-11 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 11), verbose_name='date'),
        ),
    ]