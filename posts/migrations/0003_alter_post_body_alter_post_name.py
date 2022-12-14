# Generated by Django 4.1 on 2022-08-23 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(db_index=True, default="What's Happening?", max_length=500, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=60, verbose_name='Name'),
        ),
    ]
