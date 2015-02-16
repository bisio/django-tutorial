from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from polls.models import Question

#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {'latest_question_list':latest_question_list})
    #return HttpResponse(template.render(context))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request,'polls/index.html',{'latest_question_list':latest_question_list})

def detail(request,question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question}) 

def results(request,question_id):
    response =  HttpResponse("You're looking at the results of question %s." % question_id)
    return response 


def vote(request,question_id):
    response =  HttpResponse("You're voting on question %s." % question_id)
    return response 
