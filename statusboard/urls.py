# statusboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('application/<int:app_id>/', views.application_detail, name='application_detail'),
]
