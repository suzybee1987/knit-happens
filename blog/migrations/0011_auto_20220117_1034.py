# Generated by Django 3.2 on 2022-01-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
