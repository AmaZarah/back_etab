from django.shortcuts import render

# Create your views here.
def add_teacher(request):
    return render(request, 'add_teacher.html')

def edit_teacher(request):
    return render(request, 'edit_teacher.html')

def list_teacher(request):
    return render(request, 'list_teacher.html')
