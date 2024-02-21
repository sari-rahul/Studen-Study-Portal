from django.test import TestCase
from .forms import Notesform,Homeworkform,Todoform,Commonform


class TestNotesform(TestCase):

    def test_form_is_valid(self):
        notes_form = Notesform({'title': 'test title','description': 'test description'})
        self.assertTrue(notes_form.is_valid(), msg="Form is not valid")

class TestHomeworkform(TestCase):

    def test_form_is_valid(self):
        homework_form = Homeworkform({'subject':'test subject',
                                        'title':'test title',
                                        'description':'test description',
                                        'due_date': '2024-02-21 12:00:00',
                                        'is_finished':True})
        self.assertTrue(homework_form.is_valid(), msg="Form is not valid")


class TestTodoform(TestCase):

    def test_form_is_valid(self):
        todo_form = Todoform({'title':'test title',
                              'is_completed':True})
        self.assertTrue(todo_form.is_valid(), msg="Form is not valid")


class TestCommonform(TestCase):

    def test_form_is_valid(self):
        common_form = Commonform({'search_text':'test text'})
        self.assertTrue(common_form.is_valid(), msg="Form is not valid")