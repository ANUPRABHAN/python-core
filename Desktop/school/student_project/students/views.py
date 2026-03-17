from django.shortcuts import render
from .models import Student
# in-memory list used by earlier procedural logic; can be removed or replaced with DB queries

def home(request):
    students = Student.objects.all()
    return render(request,'home.html',{'students':students})

def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'add_student.html',{'form':form})

def view_student(request):
    #form = StudentForm()
    students = Student.objects.all()
    return render(request,'viewstudent.html',{'students':students})

def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    students = Student.objects.all()
    return render(request,'delete_student.html',{'student':student})
