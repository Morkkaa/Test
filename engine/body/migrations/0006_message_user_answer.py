# Generated by Django 2.1.4 on 2019-01-04 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0005_remove_message_user_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='body.Message', verbose_name='Ответ'),
        ),
    ]
