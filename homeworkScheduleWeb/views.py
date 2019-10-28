from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    ## return HttpResponse('hello world');
    return render(request, 'todo.html')
