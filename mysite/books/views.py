from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from books.forms import ContactForm
from books.models import Book


def index(request):
    return HttpResponse('Hello')


def meta(request):
    template_name = 'books/meta.html'
    return render_to_response(template_name, {
        'meta': sorted(request.META.items())
    })


def search_form(request):
    return render_to_response('books/search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_result.html', {
                'books': books,
                'query': q
            })
        elif len(q) > 20:
            errors.append('Enter a search term.')
        else:
            errors.append('Please enter at most 20 characters.')
    return render_to_response('books/search_form.html', {'errors': errors})


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            return HttpResponseRedirect('/books/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('books/contact_form.html', {'form': form})


@csrf_exempt
def contact_thanks(request):
    return HttpResponse('thanks')


def requires_login(view):
    def new_view(request, *args, **kwargs):
        print('requires_login')
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/')
        return view(request, *args, **kwargs)

    return new_view


def my_view1(request, *args, **kwargs):
    print('my_view1')
    return HttpResponse('view1')


def my_view2(request, *args, **kwargs):
    print('my_view2')
    return HttpResponse('view2')
