# Generated by Django 3.1 on 2020-09-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice_sw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
