from django.shortcuts import render

# Create your views here.

def say_hello(request):
    context = {
        "name": "max",
        "number": 1,
        "text": "text",
    }
    return render(request, 'index.html', context)