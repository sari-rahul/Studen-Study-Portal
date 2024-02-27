from django import forms
from . models import *


class Notesform(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']


class DateInput(forms.DateInput):
    input_type = 'date'


class Homeworkform(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due_date': DateInput()}
        fields = ['subject', 'title', 'description', 'due_date', 'is_finished']


class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_completed']


class Commonform(forms.Form):
    search_text = forms.CharField(max_length=100,
                                  label='Enter your search here:')
