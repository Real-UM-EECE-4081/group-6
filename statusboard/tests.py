from django.test import TestCase
from django.urls import reverse
from .models import Application, Incident


class ApplicationDetailViewTest(TestCase):
    def setUp(self):
        self.app = Application.objects.create(name="App1", status="Running")
        self.incident = Incident.objects.create(application=self.app, description="Test Incident")

    def test_application_detail_view_status_code(self):
        """Test that the application detail view returns a 200 status code."""
        url = reverse('application_detail', args=[self.app.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_application_detail_view_contains_incident(self):
        """Test that the application detail view contains the description of an incident."""
        url = reverse('application_detail', args=[self.app.id])
        response = self.client.get(url)
        self.assertContains(response, "Test Incident")

class IncidentModelTest(TestCase):
    def setUp(self):
        self.app = Application.objects.create(name="App1", status="Running")
        self.incident = Incident.objects.create(application=self.app, description="Test Incident")

    def test_incident_creation(self):
        """Test that an incident is created successfully and linked to the correct application."""
        self.assertEqual(self.incident.description, "Test Incident")
        self.assertEqual(self.incident.application, self.app)
        self.assertFalse(self.incident.resolved)


class ExportFunctionalityTest(TestCase):
    def setUp(self):
        # Create a sample application and incident for testing
        self.app = Application.objects.create(name="Test App", status="Running")
        self.incident = Incident.objects.create(
            application=self.app,
            description="Test Incident",
            resolved=False
        )

    def test_export_csv_status_code(self):
        # Test that the export CSV URL returns a 200 status code
        url = reverse('export_application_csv', args=[self.app.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_export_csv_content(self):
        # Test that the exported CSV contains the expected incident data
        url = reverse('export_application_csv', args=[self.app.id])
        response = self.client.get(url)

        # Verify CSV headers and specific incident data
        self.assertContains(response, "Incident Description")
        self.assertContains(response, "Resolved")
        self.assertContains(response, "Occurred At")
        self.assertContains(response, "Test Incident")  # Description of the incident
        self.assertContains(response, "False")  # Resolved status
