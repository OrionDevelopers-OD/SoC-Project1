"""SoC_Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from SoC_Project1.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department, name="department"),
    path('question_papers/', views.questionppr, name="questionppr"),
    path('notes/', views.notes, name="notes"),
    path('upload/', views.upload, name="upload"),
    path('request/', views.request, name="request"),
    path('admin/', admin.site.urls)
]
