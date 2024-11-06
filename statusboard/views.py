from django.shortcuts import render, get_object_or_404
from .models import Application, Incident
from django.http import HttpResponse
import csv
# Create your views here.
def application_detail(request, app_id):
    application = get_object_or_404(Application, id=app_id)
    incidents = application.incidents.all()
    return render(request, 'statusboard/application_detail.html', {'application': application, 'incidents': incidents})

def home(request):
    return render(request, 'statusboard/home.html')

def export_application_csv(request, app_id):
    # Fetch the specific application and its related incidents
    application = get_object_or_404(Application, id=app_id)
    incidents = application.incidents.all()  # Use the related name for accessing incidents

    # Create the HTTP response with CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{application.name}_incidents.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    writer.writerow(['Incident Description', 'Resolved', 'Occurred At'])

    # Write each incident's data to the CSV file
    for incident in incidents:
        writer.writerow([incident.description, incident.resolved, incident.occurred_at])

    return response

