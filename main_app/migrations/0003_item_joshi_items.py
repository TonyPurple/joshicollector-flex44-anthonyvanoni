# Generated by Django 4.0.1 on 2022-02-05 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_joshi_aerial_joshi_itfactor_joshi_power_joshi_speed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='joshi',
            name='items',
            field=models.ManyToManyField(to='main_app.Item'),
        ),
    ]
