# Generated by Django 4.1 on 2023-03-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_post_no_comments_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.CharField(max_length=500),
        ),
    ]
