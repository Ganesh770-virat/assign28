from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def siraj(request):
    return HttpResponse('<h1>siraj is my fav bowler')
