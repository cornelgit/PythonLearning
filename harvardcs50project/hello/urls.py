from django.urls import path
from . import views

# a list of all allowable urls accessible for this particular app
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("cornel", views.cornel, name="cornel"),
    path("jessica", views.jessica, name="jessica"),
]