from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .models import Message, Tag
from django.views.generic import View
from .utils import *
from .forms import *
from django.urls import reverse
from datetime import datetime, timedelta
from django.http import HttpResponse


def messages_list(request):
    messages=Message.objects.order_by('-id')
    return render(request, 'test.html', context={'messages': messages, 'username': auth.get_user(request)})

class MessageCreate(ObjectCreateMixin, View):
    form_model = MessageForm
    template = 'message_create.html'

class MessageUpdate(ObjectUpdateMixin, View):
    model = Message
    model_form = MessageForm
    template = 'message_update.html'

class MessageDetail(ObjectDetailMixin, View):
    model = Message
    template = 'message_detail.html'

class MessageDelete(ObjectDeleteMixin, View):
    model = Message
    template = 'message_delete.html'
    redirect_url = 'test_html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'tag_detail.html'

class TagCreate(ObjectCreateMixin, View):
   form_model = TagForm
   template = 'tag_create.html'

class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'tag_update.html'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'tag_delete.html'
    redirect_url = 'tags_list_url'

def tags_list(request):
    tags=Tag.objects.all()
    return render(request,'tags_list.html', context={'tags':tags})



class MessageAnswer(View):
    def get(self, request, slug):
        user_answer=Message.objects.get(slug__iexact=slug)
        boound_form = AnswerForm(instance=user_answer)

        return render(request, 'message_answer.html',context={'form': boound_form, 'user_answer':user_answer})

    def post(self, request, slug):
        user_answer = Message.objects.get(slug__iexact=slug)
        boound_form = AnswerForm(request.POST, instance=user_answer)

        if boound_form.is_valid():
            new_answer = boound_form.save()
            return redirect(new_answer)

        return render(request, 'user_answer_url', context={'form': boound_form, 'user_answer': user_answer})





