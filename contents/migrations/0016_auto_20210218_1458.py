# Generated by Django 3.1.4 on 2021-02-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0015_auto_20210210_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='content_imgs'),
        ),
    ]