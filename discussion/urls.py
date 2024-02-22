from . import views
from django.urls import path

urlpatterns = [
    path('', views.discussion.as_view(), name='question'),
]