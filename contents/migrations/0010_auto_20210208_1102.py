# Generated by Django 3.1.4 on 2021-02-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0009_auto_20210208_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='servises',
            field=models.ManyToManyField(to='contents.Service'),
        ),
    ]
