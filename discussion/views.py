from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import AnswerForm
from django.shortcuts import render, get_object_or_404

from .models import Question ,Answer
# Create your views here.

class discussion (generic.ListView):
    queryset = Question.objects.all().order_by("created_on")
    paginate_by = 6
    template_name = "discussion/question_list.html"



def a_discussion_form(request, title):
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
            messages.add_message(
            request, messages.SUCCESS,
            'Answer submitted successfully!!')

    answer_form = AnswerForm()
    context = {"answer_form": answer_form,
               "question": question,
               "answers": answers,
               "answer_count":answer_count,}
    return render(request,"discussion/a_discussion_form.html", context)

    """def post_detail(request, slug):
    

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
    )


    comment_form = CommentForm()


    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )"""