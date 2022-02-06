# Generated by Django 4.0.1 on 2022-02-05 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_item_joshi_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='booking date')),
                ('booking', models.CharField(choices=[('D', 'Dojo Training'), ('S', 'Singles Match'), ('T', 'Tag Match'), ('U', 'Unit Match'), ('G', 'Gimmick Match'), ('M', 'Media Appearance')], default='D', max_length=1)),
                ('joshi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.joshi')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]