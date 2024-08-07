from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("this is a response")


def edit_profile(request):
    return HttpResponse("this is a edit")
