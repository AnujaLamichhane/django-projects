from django.shortcuts import render

# Create your views here.
def index(request):
    context= {
        # "page_title" : "django day 3",
        # "message" : "welcome"
    }
    return render (request,'homepage/home.html', context)

def about(request):
    context= {
      
        # "message" : "this is about"
    }
    return render (request,'homepage/about.html', context)
def skills(request):
    context= {
      
        # "message" : "this is about"
    }
    return render (request,'homepage/skills.html', context)

def contact(request):
    context = {
        
       # "message": "skill page!"
    }
    return render(request, 'homepage/contact.html', context)