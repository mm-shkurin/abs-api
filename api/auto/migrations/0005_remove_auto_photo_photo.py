# Generated by Django 5.0 on 2024-09-13 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_alter_auto_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='photo',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='auto.auto')),
            ],
        ),
    ]
