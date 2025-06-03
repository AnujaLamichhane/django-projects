# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# def index(request):
#     # return HttpResponse("this is my homepage")
#     context={

#     }
#     template_name='homepage/home.html'
#     return render(request,template_name)
    
def about(request):
   return HttpResponse("this is myabout page")

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "page_title": "Django Day 2",
        "message": "Welcome to Day 2 of Django!"
    }
    return render(request, 'homepage/home.html', context)

def greet(request , name ):
    # context = {'name': 'Alice'  # Or get this from URL/query params etc.
    # }
    return render(request, 'homepage/greet.html', {'name':name})

   

def profile(request):
    user_data = {
        "name": "Sabina",
        "email": "sabina@example.com",
        "hobbies": ["Coding", "Reading", "Traveling"]
    }
    return render(request, 'homepage/profile.html', user_data)


