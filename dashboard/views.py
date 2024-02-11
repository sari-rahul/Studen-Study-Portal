from django.shortcuts import render
from . models import Note
# Create your views here.

def home (request):
    return render (request,"dashboard/home.html")

def notes (request):
    note = Note.object.filter(user=request.user)
    context ={'notes':notes}
    return render (request,"dashboard/notespage.html",context)