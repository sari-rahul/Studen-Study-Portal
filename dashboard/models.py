from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# ---------------------------------------------------------NOTES MODEL
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


# ---------------------------------------------------------HOMEWORK MODEL
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# ---------------------------------------------------------To-Do MODEL
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
