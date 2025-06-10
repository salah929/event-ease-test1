from django.shortcuts import render
from django.http import HttpResponse


def events(request):
    return HttpResponse("Welcome to Events!")
