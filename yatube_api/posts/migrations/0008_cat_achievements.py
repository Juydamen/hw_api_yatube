# Generated by Django 3.2.16 on 2023-05-08 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_cat_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='achievements',
            field=models.ManyToManyField(through='posts.AchievementCat', to='posts.Achievement'),
        ),
    ]
