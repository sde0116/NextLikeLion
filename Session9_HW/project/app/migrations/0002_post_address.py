# Generated by Django 4.0.4 on 2022-05-12 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.URLField(default=''),
        ),
    ]
