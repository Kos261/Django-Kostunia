from django.shortcuts import render
from django.http.response import HttpResponse
from .models import ToDoList, Item
# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {"name":"Test"})

def create(response):
    return render(response, "main/create.html", {})


# def index(response, id):
#     ls = ToDoList.objects.get(id=id)
#     items = list(ls.item_set.all())  # Zamień na listę
#     if items:
#         item = items[0]  # Pobierz pierwszy element
#         return HttpResponse("<h1>Kostunio hehe  %s </h1> <br></br> <p>%s</p>" % (ls.name, str(item.text)))
#     else:
#         return HttpResponse("<h1>Kostunio hehe  %s </h1> <br></br> <p>Brak elementów w liście ToDo</p>" % (ls.name))


# def v1(response):
#     return HttpResponse("<h1>view1</h1>")