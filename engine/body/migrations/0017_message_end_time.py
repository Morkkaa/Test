# Generated by Django 2.1.4 on 2019-01-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0016_auto_20190113_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='End_Time'),
        ),
    ]
