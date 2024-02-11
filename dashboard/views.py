from django.shortcuts import render
from . models import Note
# Create your views here.

def home (request):
    return render (request,"dashboard/home.html")

def notes (request):
    notes = Note.objects.filter(user=request.user)
    context ={'notes':notes}
    return render (request,"dashboard/notes.html",context)