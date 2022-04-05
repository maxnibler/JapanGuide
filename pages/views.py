from django.shortcuts import render
from django.core.management.utils import get_random_secret_key

# Create your views here.

def say_hello(request):
    context = {
        "name": "maxnibler",
        "number": 1,
        "text": "text",
    }
    return render(request, 'pages/home.html', context)

def home(request):
    context = {

    }
    return render(request, 'pages/home_page.html', context)
    
def account(request):
    context = {}
    return render(request, 'pages/account_page.html', context)