# Generated by Django 3.1.4 on 2021-01-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_service_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ManyToManyField(to='contents.Category'),
        ),
    ]
