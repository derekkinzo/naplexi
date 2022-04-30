from django.shortcuts import render

# Create your views here.

def index(request):
    print("Request for index page received")

    context = {}
    return render(request, 'flashcards/index.html', context)