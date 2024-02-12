from django.shortcuts import render
from django.contrib import messages
from . forms import *
# Create your views here.

def home (request):
    return render (request,"dashboard/home.html")

def notes (request):
    if request.method == "POST":
        form = Notesform(request.POST)
        if form.is_valid():
            notes = Note(
                user=request.user,title=request.POST['title'],
                description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added successfully from {request.user.username}")
    else:
        form = Notesform()

    notes = Note.objects.filter(user=request.user)
    context ={'notes':notes,'form':form}
    return render (request,"dashboard/notes.html",context)