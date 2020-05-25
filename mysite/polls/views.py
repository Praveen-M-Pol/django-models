from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {
        'latest_questions':latest_questions
    })

def detail(request, question_id):
    return HttpResponse('This is the detailed view of the question: %s' % question_id)

def results(request, question_id):
    return HttpResponse('This is the results of the question: %s' % question_id)

def vote(request, question_id):
    return HttpResponse('vote on question: %s' % question_id)

