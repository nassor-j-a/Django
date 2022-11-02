from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response || request handler || action

# function use
# pull data from a database
# send email
# transform data
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Django Template'})