# Generated by Django 3.1.4 on 2021-01-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_auto_20210113_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]