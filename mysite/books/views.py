from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book

# Create your views here.


def index(request):
    return HttpResponse('Hello')


def meta(request):
    template_name = 'books/meta.html'
    return render_to_response(template_name,
                              {'meta': sorted(request.META.items())})


def search_form(request):
    return render_to_response('books/search_form.html')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_result.html',
                                      {'books': books,
                                       'query': q})
        else:
            error = True
    return render_to_response('books/search_form.html', {'error': error})
