# Generated by Django 5.0 on 2024-09-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]