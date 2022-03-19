from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.




# def index(response, id):
#     ls = ToDoList.objects.get(id=id)
#     items = ls.item_set.get(id=1)
#     return render(response, "main/base.html", {})


def list(req, id):
    todo = ToDoList.objects.get(id=id)
    context =  {
        "ls":todo
    }
    return render(req, "main/list.html", context)

def home(req):
    return render(req, "main/home.html", {})

