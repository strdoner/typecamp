# Generated by Django 4.2.3 on 2024-05-27 15:19

from django.db import migrations, models
import typecamp_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('typecamp_app', '0004_alter_profile_user_delete_usertmp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_stat',
            field=models.JSONField(default=typecamp_app.models.total_stat_default, verbose_name='total_stats'),
        ),
    ]