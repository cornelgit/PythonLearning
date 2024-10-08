from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # takes in http request object
    return render(request, "hello/index.html") # instead of a string, rendering an entire html file


def cornel(request):
    return HttpResponse("Hello, Cornel!")


# we can add more views
def jessica(request):
    return HttpResponse("Hello, Jessica!")

# more dynamic
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })