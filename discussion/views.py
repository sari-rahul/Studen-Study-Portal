from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, reverse
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm


# Create your views here.

class discussion (generic.ListView):
    queryset = Question.objects.all().order_by("-created_on")
    paginate_by = 9
    template_name = "discussion/question_list.html"


@login_required
def ask_a_question(request):
    """
    A form to ask Questions
    """
    if request.method == "POST":
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            question = Question(
                author=request.user,
                title=request.POST['title'],
                content=request.POST['content'])
            question.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Question submitted successfully!!')
    else:
        question_form = QuestionForm()

    question = Question.objects.filter(author=request.user.id)
    context = {"form": question_form,
               "question": question,
               }
    return render(request, "discussion/ask_a_question.html", context)


def a_discussion_form(request, title):
    """
    Discussion forum single page view
    """
    queryset = Question.objects.all()
    question = get_object_or_404(queryset, title=title)
    answers = question.answers.all().order_by("-created_on")
    answer_count = question.answers.count()
    if request.method == "POST":
        answer_form = AnswerForm(data=request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Answer submitted successfully!!')

    answer_form = AnswerForm()
    context = {"answer_form": answer_form,
               "question": question,
               "answers": answers,
               "answer_count": answer_count, }
    return render(request, "discussion/a_discussion_form.html", context)


@login_required
def answer_edit(request, title, answer_id):
    """
    view to edit answers
    """
    if request.method == "POST":

        queryset = Question.objects.all()
        question = get_object_or_404(queryset, title=title)

        answer = get_object_or_404(Answer, pk=answer_id)
        answer_form = AnswerForm(data=request.POST, instance=answer)

        if answer_form.is_valid() and answer.author == request.user:
            answer = answer_form.save()
            answer.question = question
            answer.save()
            messages.add_message(request, messages.SUCCESS, 'Answer Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating Answers!')

    return HttpResponseRedirect(reverse('a-discussion-form', args=[title]))


@login_required
def answer_delete(request, title, answer_id):
    """
    view to delete answer
    """
    queryset = Question.objects.all()
    question = get_object_or_404(queryset, title=title)
    answer = get_object_or_404(Answer, pk=answer_id)

    if answer.author == request.user:
        answer.delete()
        messages.add_message(request, messages.SUCCESS, 'Answer deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own Answers!')

    return HttpResponseRedirect(reverse('a-discussion-form', args=[title]))
