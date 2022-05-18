# Generated by Django 3.1.1 on 2022-05-14 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='city',
        ),
        migrations.RemoveField(
            model_name='service',
            name='id',
        ),
        migrations.AddField(
            model_name='service',
            name='hospital',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.hospital'),
        ),
        migrations.AddField(
            model_name='service',
            name='oxygen_cyliender_total',
            field=models.IntegerField(default=0),
        ),
    ]
