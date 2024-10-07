from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # takes in http request object
    return HttpResponse("Hello!")


def cornel(request):
    return HttpResponse("Hello, Cornel!")


# we can add more views
def jessica(request):
    return HttpResponse("Hello, Jessica!")

# more dynamic
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")