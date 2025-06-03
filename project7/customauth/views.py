from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def dashboard(request):
    return HttpResponse("you can view this")


# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponse("you are not allowed to view this")
    context = {}
    return render(request,"customauth/profile.html",context)


def good(request):
    if  request.user.is_authenticated:
        return HttpResponse("ancd1234")
    context = {}
    return render(request,"customauth/good.html",context)