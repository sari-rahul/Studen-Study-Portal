from django.urls import path
from . import views

urlpatterns= [
#--------------------------------------------------------------------------------urls for Notes page
    path('',views.home, name= "home"),
    path('notes',views.notes, name= "notes"),
    path('delete_notes/<int:pk>',views.delete_notes,name= "delete-notes"),
    path('notes_detail/<int:pk>',views.notes_detail_view.as_view(),name= "notes-detail"),

#--------------------------------------------------------------------------------urls for Homeworks page
    path('homeworks',views.homework, name="homeworks"),
    path('delete_homework/<int:pk>',views.delete_homework,name= "delete-homework"),
    path('update_homework/<int:pk>',views.update_homework,name= "update-homework"),
    path('homework_detail_view/<int:pk>',views.homework_detail_view.as_view(),name= "homework-detail"),

#--------------------------------------------------------------------------------url for YouTube search page
    path('youtube_search',views.youtube_search, name="youtube_search"),

#--------------------------------------------------------------------------------url todo page
    path('todo',views.todo, name="todo"),
    path('delete_todo_list/<int:pk>',views.delete_todo_list,name="delete-todo"),
    path('update_todo_list/<int:pk>',views.update_todo_list,name= "update-todo"),
    
]