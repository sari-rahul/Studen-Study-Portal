from .models import Answer, Question
from django import forms


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
