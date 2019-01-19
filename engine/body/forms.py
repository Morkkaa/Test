from django import forms
from .models import *
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    class Meta:
        model=Tag
        fields=['text', 'slug']

        widgets={
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug=='create':
            raise ValidationError('Slug may mot be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))

        return new_slug

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['text', 'slug', 'real_answer', 'tags']

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'real_answer': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may mot be "Create"')
        return new_slug

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['user_answer']

        widgets={
            'user_answer' : forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may mot be "Create"')
        return new_slug

'''
class AnswerF(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['answer', 'date', 'end_time']

        widgets={
            'answer': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateTimeField(attrs={'class': 'form-control'}),
            'end_time': forms.DateTimeField(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may mot be "Create"')
        return new_slug
'''