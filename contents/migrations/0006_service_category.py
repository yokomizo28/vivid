# Generated by Django 3.1.4 on 2021-01-13 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_content_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contents.category'),
            preserve_default=False,
        ),
    ]
