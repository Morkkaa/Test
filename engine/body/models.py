from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from time import *

def gen_slug(s):
    new_slug=slugify(s, allow_unicode=True)
    return new_slug+'-'+str(int(time()))



class Message(models.Model):
    text = models.TextField('Сообщение', max_length=500)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    real_answer = models.TextField('real_answer', max_length=150)
    tags = models.ManyToManyField('Tag', blank=True, related_name='messages')
    date = models.DateTimeField('Дата', auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    user_answer = models.TextField('Ответ пользователя', max_length=500, null=True)


    def get_absolute_url(self):
        return reverse('message_detail_url', kwargs={'slug': self.slug})



    def get_delete_url(self):
        return reverse('message_delete_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('message_update_url', kwargs={'slug': self.slug})

    def get_answer_url(self):
        return reverse('message_answer_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug=gen_slug(self.text)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.text)

class Tag(models.Model):
    text=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.text


class Answer(models.Model):
    text=models.IntegerField()
    date=models.DateTimeField('Дата создания ответа', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.answer


