# Generated by Django 2.1.4 on 2019-01-05 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0009_remove_message_user_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]
