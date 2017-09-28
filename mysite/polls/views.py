# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.http import Http404
from models import Question, Choice


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def tribute(request):
    return render(request, "polls/tribute-page.html")


def detail(request, question_id):
    # try:
        # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist as e:
        # raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) as e:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You don't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
