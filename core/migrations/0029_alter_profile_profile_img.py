# Generated by Django 4.1 on 2023-03-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='defualt-user.png', upload_to='profile_images'),
        ),
    ]
