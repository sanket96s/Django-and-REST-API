from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def home(request):
    return HttpResponse("Hello ! this is starting of functional view")

class HomeView(View):
    def get(self, request):
        return HttpResponse("welcome to the class based home view")
