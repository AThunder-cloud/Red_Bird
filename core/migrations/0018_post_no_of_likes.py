# Generated by Django 4.1 on 2023-03-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_like_post_remove_like_user_like_post_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
