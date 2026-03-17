from django.shortcuts import render

# Create your views here.
def home(request):
    task = ["Go to the gym", "Buy groceries", "Read a book", "Call a friend", "Write a blog post"]
    return render(request, 'home.html')