# Generated by Django 3.1.6 on 2021-03-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0004_auto_20210318_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(blank=True, default='', verbose_name='location'),
        ),
    ]
