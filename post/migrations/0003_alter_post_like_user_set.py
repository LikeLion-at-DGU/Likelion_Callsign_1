# Generated by Django 4.0.4 on 2022-11-16 14:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('post', '0002_alter_post_count_alter_post_countb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='likes_user_set', through='post.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]