# Generated by Django 4.0.1 on 2022-02-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joshi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('promotion', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('finisher', models.CharField(max_length=100)),
            ],
        ),
    ]
