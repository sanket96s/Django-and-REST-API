from django.shortcuts import render
from django.http import HttpResponse

def profile(request,username):
    return HttpResponse(f"profile age of {username}")

def html_view(request):
    return render(request,"home.html")