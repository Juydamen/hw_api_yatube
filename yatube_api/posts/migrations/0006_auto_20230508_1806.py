# Generated by Django 3.2.16 on 2023-05-08 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20230508_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='achievements',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='owner',
        ),
    ]
