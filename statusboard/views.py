from django.shortcuts import render, get_object_or_404
from .models import Application
# Create your views here.
def application_detail(request, app_id):
    application = get_object_or_404(Application, id=app_id)
    incidents = application.incidents.all()
    return render(request, 'statusboard/application_detail.html', {'application': application, 'incidents': incidents})

def home(request):
    return render(request, 'statusboard/home.html')
