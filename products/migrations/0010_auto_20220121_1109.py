# Generated by Django 3.2 on 2022-01-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_title',
            field=models.TextField(max_length=254),
        ),
    ]
