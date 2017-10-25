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
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_result.html',
                                      {'books': books,
                                       'query': q})
        elif len(q) > 20:
            errors.append('Enter a search term.')
        else:
            errors.append('Please enter at most 20 characters.')
    return render_to_response('books/search_form.html', {'errors': errors})
