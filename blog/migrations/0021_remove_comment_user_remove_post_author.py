# Generated by Django 5.0.1 on 2024-02-12 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
