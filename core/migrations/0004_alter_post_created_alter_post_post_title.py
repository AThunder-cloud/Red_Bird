# Generated by Django 4.1 on 2022-12-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_options_post_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(default='No title', max_length=20),
        ),
    ]
