from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
from . forms import *

# Create your views here.
# ---------------------------------------------------------HOME VIEWS
def home (request):
    '''
    View for the Home Page.

    '''
    return render (request,"dashboard/home.html")


# ---------------------------------------------------------NOTES PAGE VIEWS
def notes (request):
    '''
    View for Adding Notes and displaying success message.

    '''
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
    '''
    View for Deleting notes and displaying success message.


    '''
    del_note = Note.objects.filter(id=pk) 
    del_note.delete()
    return redirect("/notes")

class notes_detail_view(generic.DetailView):
    '''
    View for the Detailed view of each Notes

    '''
    model = Note
    template_name = 'dashboard/notes_detail.html' 

# ---------------------------------------------------------HOMEWORKS PAGE VIEWS
def homework (request):
    '''
    View for the Home Page and creating new homeworks.

    '''
    if request.method == "POST":
        form = Homeworkform(request.POST)
        if form.is_valid():
            try:
                finished= request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homework = Homework(
                user= request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due_date=request.POST['due_date'],
                is_finished=finished
                )
            homework.save()
            messages.success(request,f"Home work added successfully!!!!")

    else:
        form = Homeworkform()  

    homework = Homework.objects.filter(user=request.user.id)
    if len(homework) == 0:
        homework_completed = True
    else:
        homework_completed = False

    context = {'homeworks':homework,
                'homework_completed':homework_completed,
                'form':form,}
    return render (request,"dashboard/homework.html",context)



def delete_homework(request,pk=None):
    '''
    View for Deleting homeworks and displaying success message.


    '''
    del_homework = Homework.objects.filter(id=pk) 
    del_homework.delete()
    messages.success(request,f"Home work deleted successfully!!!!")
    return redirect("/homeworks")


def update_homework(request,pk=None):
    '''
    View for Updating the status of Homework done and displaying success message.


    '''
    homework = Homework.objects.get(id=pk) 
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    messages.success(request,f"Home work updated successfully!!!!")
    return redirect("/homeworks")


class homework_detail_view(generic.DetailView):
    '''
    View for the Detailed view of each Homework
    '''
    model = Homework
    template_name = 'dashboard/homework_detail_view.html'


# ---------------------------------------------------------YOUTUBE PAGE VIEWS
def youtube_search(request):
    '''
    View to search videos in Youtube
    '''
    if request.method == 'POST':
        form = Commonform(request.POST)
        search_text = request.POST['search_text']
        video = VideosSearch(search_text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict={
                'input':search_text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description']= desc
            result_list.append(result_dict)
            context = {
                'form':Commonform,
                'results':result_list
            }
        return render(request,"dashboard/youtube_search.html",context)
    else:
        form = Commonform
    context = {
        'form':form
    }

    return render(request,"dashboard/youtube_search.html",context)