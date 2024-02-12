from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic
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

    notes = Note.objects.filter(user=request.user.id)
    context ={'notes':notes,'form':form}
    return render (request,"dashboard/notes.html",context)


def delete_notes(request,pk=None):
    del_note = Note.objects.filter(id=pk) 
    del_note.delete()
    return redirect("/notes")



class notes_detail_view(generic.DetailView):
    model = Note
    template_name = 'dashboard/notes_detail.html' 
