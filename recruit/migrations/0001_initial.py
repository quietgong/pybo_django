# Generated by Django 3.1 on 2020-09-06 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Recruit_author_answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.TextField()),
                ('specific_id', models.CharField(max_length=15)),
                ('content', models.TextField()),
                ('date', models.CharField(max_length=20)),
                ('voter', models.ManyToManyField(blank=True, related_name='Recruit_voter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruit.answer')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Recruit_comment_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit.post'),
        ),
        migrations.AddField(
            model_name='answer',
            name='voter',
            field=models.ManyToManyField(related_name='Recruit_voter_answer', to=settings.AUTH_USER_MODEL),
        ),
    ]
