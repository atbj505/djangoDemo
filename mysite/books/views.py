from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello')


def meta(request):
    template_name = 'books/meta.html'
    return render_to_response(template_name,
                              {'meta': sorted(request.META.items())})
