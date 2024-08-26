from django.shortcuts import render

# Create your views here.
def add_student(request):
    return render(request, 'add_student.html')

def edit_student(request):
    return render(request, 'edit_student.html')

def list_student(request):
    return render(request, 'list_student.html')