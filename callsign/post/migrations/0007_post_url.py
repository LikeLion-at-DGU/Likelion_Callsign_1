# Generated by Django 4.0.3 on 2022-10-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_sex_post_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(default='', max_length=300),
        ),
    ]
