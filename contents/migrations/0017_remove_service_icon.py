# Generated by Django 3.1.4 on 2021-02-27 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0016_auto_20210218_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
    ]
