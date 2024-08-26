from django.shortcuts import render

# Create your views here.
def add_user(request):
    return render(request, 'add_user.html')

def edit_user(request):
    return render(request, 'edit_user.html')

def list_user(request):
    return render(request, 'list_user.html')
