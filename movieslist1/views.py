from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def darling(request):
    return HttpResponse('<h1>i am die hard fan of prabhas</h1>')
def darlings(request):
    return HttpResponse('<h1>my fav movie of prabhas is saalar </h1>')

