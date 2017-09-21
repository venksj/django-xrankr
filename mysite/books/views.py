from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    if 'q' in request.POST:
        message = 'You searched for: %r' %(request.POST['q'])
    else:
        message = "Empty form submitted"
    return HttpResponse(message)


