# Generated by Django 4.0.1 on 2022-02-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joshi',
            name='aerial',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='joshi',
            name='itfactor',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='joshi',
            name='power',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='joshi',
            name='speed',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='joshi',
            name='striking',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='joshi',
            name='technique',
            field=models.IntegerField(default=50),
        ),
    ]
