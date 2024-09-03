#from django.http import HttpResponse
from django.shortcuts import render
def homepage(req):
    #return HttpResponse('Hello World!! I am Ashu')
    return render(req, 'home.html')
