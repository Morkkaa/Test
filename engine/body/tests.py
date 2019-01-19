from django.test import TestCase


'''
class MassageView(View):
    
    def get(self, request):
        messages = Message.objects.filter(user_answer__isnull=True)
        form=MessageForm()
        return render(request, 'test.html', {'messages': messages, 'username': auth.get_user(request), 'form': form})

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            pk=request.POST.get('id', None)
            form=form.save(commit=False)
            try:
                form.user_answer=Message.objects.get(id=pk)
            except:
                pass
            form.user=request.user
            form.save()
            return redirect('/')
        else:
            return HttpResponse('error')


{% if user.is_active %}
    <form action="" method="post">
        {% csrf_token %}
        <input type="number" name="id" hidden value="{{post.id}}">
        {{ form.as_p }}
        <button type="submit">Отправить</button>
    </form>
{% endif %}
'''

'''
class MassageView(View):

    def get(self, request):
        messages = Message.objects.all()
        form=MessageForm()
        return render(request, 'test.html', {'messages': messages, 'username': auth.get_user(request), 'form': form})

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('/')
        else:
            return HttpResponse('error')

class AnswerView(View):
    def get(self,request):
        answer=Answer.objects.all()
        form=AnswerForm
        return render(request,'test.html', {'answer':answer, 'form':form})

    def post(self, request):
        form = AnswerForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('/')
        else:
            return HttpResponse('error')
'''