from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return HttpResponse("<h1>Hello World!</h1>")


def home(request):
    return HttpResponse("<h1>This is Homepage</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")


'''
'/' mean home url
'/about' mean first home url + about    
                                    that mean about will place after home url
'''


def contact(request):
    return HttpResponse("<h1>THis is Contact Page</h1> <a href='/'>Homepage</a> <a href='/about/'>About</a>")


def about(request):
    return HttpResponse("<h1>About us</h1> <a href='/'>Homepage</a> <a href='/contact/'>Cantact</a>")
