from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. <div>kot</div>You're at the polls index.")


def index1(request):
    return HttpResponse("asd")