from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("Hello")


def start(response):
    return HttpResponse("Startinggg")

def v1(response):
    return HttpResponse("version 1")