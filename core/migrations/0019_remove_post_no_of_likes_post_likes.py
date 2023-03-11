# Generated by Django 4.1 on 2023-03-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_post_no_of_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='no_of_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(to='core.like'),
        ),
    ]