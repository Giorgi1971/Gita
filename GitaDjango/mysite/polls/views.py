from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DeleteView, DetailView, UpdateView


def home(request):
    return render(request, 'polls/home.html')

class QuestionListView(ListView):
    model = Question
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}


class QuestionDetailView(DetailView):
    model = Question


class QuestionResultView(DetailView):
    model = Question
    template_name = 'polls/question_result.html'


def vote(request, pk):
    quest = Question.objects.get(pk=pk)
    print(request.POST)
    try:
        pkc = request.POST['vote']
    except:
        return render(request, 'polls/question_detail.html', {
        'object': quest,
        'error_message': "You didn't select a choice.",
        })

    chos = quest.choices.get(pk=pkc)
    chos.votes += 1
    chos.save()
    return HttpResponseRedirect(reverse('polls:results', args=[pk]))