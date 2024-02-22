from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Question ,Answer
# Create your views here.

class discussion(generic.ListView):
    model = Question