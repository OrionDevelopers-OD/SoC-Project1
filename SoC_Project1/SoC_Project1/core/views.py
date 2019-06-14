from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def department(request):
    return render(request, 'department.html')

def subject(request):
    return render(request, 'subject.html')

def questionppr(request):
    return render(request, 'questionppr.html')

def notes(request):
    return render(request, 'notes.html')

def upload(request):
    return render(request, 'upload.html')

def request(request):
    return render(request, 'request.html')


