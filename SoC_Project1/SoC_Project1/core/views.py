from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')

def department(request):
    return render(request, 'department.html')

def questionppr(request):
    return render(request, 'questionppr.html')

def notes(request):
    return render(request, 'notes.html')

class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def request(request):
    return render(request, 'request.html')

#class CreateDepartmentView():
#    model = Department
##    template_name = 'template.html'
