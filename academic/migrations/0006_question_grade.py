# Generated by Django 3.1 on 2020-08-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_auto_20200828_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.CharField(default='공통', max_length=10),
        ),
    ]
