from django.urls import path
from . import views

urlpatterns= [

    path('',views.home, name= "home"),
    path('notes',views.notes, name= "notes"),
    path('delete_notes/<int:pk>',views.delete_notes,name= "delete-notes"),
    path('notes_detail/<int:pk>',views.notes_detail_view.as_view(),name= "notes-detail"),
    path('homeworks',views.homework, name= "homework"),
    path('delete_homework/<int:pk>',views.delete_homework,name= "delete-homework"),
]