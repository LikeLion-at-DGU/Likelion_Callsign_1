# Generated by Django 4.1.2 on 2022-10-09 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='writer',
        ),
    ]