from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello! students,Welcome to Django")
    return render(request,'front/index.html')