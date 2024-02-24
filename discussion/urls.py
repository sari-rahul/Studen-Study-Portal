from . import views
from django.urls import path

urlpatterns = [
    path('', views.discussion.as_view(), name='discussion'),
    path('a_discussion_form/<title>/', views.a_discussion_form, name='a-discussion-form'),
    path('a_discussion_form/<title>/edit_answer/<int:answer_id>',
         views.answer_edit, name='answer-edit'),
    path('a_discussion_form/<title>/delete_answer/<int:answer_id>',
         views.answer_delete, name='answer-delete'),
]