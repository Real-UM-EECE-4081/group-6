from django.test import TestCase
from django.urls import reverse
from .models import Application

class ApplicationModelTest(TestCase):
    def setUp(self):
        self.app = Application.objects.create(name="App1", status="Running")

    def test_application_creation(self):
        """Test that an application is created successfully with the correct name and status."""
        self.assertEqual(self.app.name, "App1")
        self.assertEqual(self.app.status, "Running")

    def test_application_str_method(self):
        """Test the __str__ method of the Application model."""
        self.assertEqual(str(self.app), "App1")

class DashboardViewTest(TestCase):
    def setUp(self):
        Application.objects.create(name="App1", status="Running")
        Application.objects.create(name="App2", status="Error")

    def test_dashboard_view_status_code(self):
        """Test that the dashboard view returns a 200 status code."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_contains_applications(self):
        """Test that the dashboard view contains the names of applications."""
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, "App1")
        self.assertContains(response, "App2")