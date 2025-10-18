from django.shortcuts import render
from django.http import HttpResponse
 
def welcome(request, name):
    """
    A simple Django view that takes a name from the URL
    and returns a personalized welcome message.
    """
    context = {
        'name': name
    }
    return render(request, 'activity/welcome.html', context)