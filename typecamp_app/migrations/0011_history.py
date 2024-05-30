# Generated by Django 4.2.3 on 2024-05-30 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('typecamp_app', '0010_post_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateTimeField(auto_now=True)),
                ('wpm', models.IntegerField(default=0)),
                ('lpm', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('mistakes', models.IntegerField(default=0)),
                ('accuracy', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
