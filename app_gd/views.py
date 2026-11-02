from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest, HttpHeaders


# Create your views here.
def index(request: HttpRequest):
    context = {"text": "Hello My Dear World"}
    return render(request, 'index.html', context=context)
