from . import views
from django.urls import path

urlpatterns = [
    path('', views.discussion.as_view(), name='discussion'),
    path('a_discussion_form/<title>/', views.a_discussion_form, name='a-discussion-form'),
]