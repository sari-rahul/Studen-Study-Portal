from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import Notesform,Homeworkform,Todoform,Commonform
from .models import Note,Homework,Todo


# Create your tests here.
class TestDashboardViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            id="1",
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.note = Note(user=self.user,
                         title="Test title", 
                         description="Description content")
        self.note.save()

    def test_successful_notes_submission(self):
        """Test for posting notes"""
        self.client.login(
            id="1",username="myUsername", password="myPassword")
        notes = {
            'title':'This is a testdata.',
            'description': 'This is a test description.'
        }
        response = self.client.post(reverse(
            'notes'), notes)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Notes added successfully from myUsername account',
            response.content
        )

    def test_successful_homework_submission(self):
        """Test for posting a homework """
        self.client.login(
            id="1",username="myUsername", password="myPassword")
        homework = {
            'subject':'Test subject',
            'title':'This is a testdata.',
            'description': 'This is a test description.',
            'due_date':'2024-02-21 12:00:00',
            'is_finished':False
        }
        response = self.client.post(reverse(
            'homeworks'), homework)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Home work added successfully!!!!',
            response.content
        )


    def test_successful_todo_submission(self):
            """Test for posting a homework """
            self.client.login(
                id="1",username="myUsername", password="myPassword")
            todo = {
                'title':'This is a testdata.',
                'is_completed':False
            }
            response = self.client.post(reverse(
                'todo'), todo)
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                b'Items added to To-Do list from myUsername!!!',
                response.content
            )
