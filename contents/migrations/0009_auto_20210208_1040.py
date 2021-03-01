# Generated by Django 3.1.4 on 2021-02-08 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_content_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='series',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ImageField(default=1, upload_to='service_icons'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='content-imgs'),
        ),
    ]
