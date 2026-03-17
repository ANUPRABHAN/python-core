from django.shortcuts import render

# Create your views here.
def home(request):
    tasks = ["Shopping","Cleaning","Sleep","Play","Trip"]
    return render(request,'todoapp/opt.html',{'tasks':tasks})