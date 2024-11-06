from django.shortcuts import render
from .models import Application

def dashboard(request):
    applications = Application.objects.all()
    return render(request, 'statusboard/dashboard.html', {'applications': applications})
