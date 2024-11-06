# statusboard/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    #path('statusboard/', include('statusboard.urls')),
    path('application/<int:app_id>/', views.application_detail, name='application_detail'),
    path('application/<int:app_id>/csv/', views.export_application_csv, name='export_application_csv'),
]
