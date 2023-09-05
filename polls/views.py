from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import Http404
from django.template import loader


from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(context, request)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question unvaillable at the moment')
    return HttpResponse(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    response = "Your are on result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Your voting for question %s." % question_id)
