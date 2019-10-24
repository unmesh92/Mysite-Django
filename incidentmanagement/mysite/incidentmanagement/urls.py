from django.urls import path

from . import views

urlpatterns = [
    path('', views.IncidentDetailsRetrieveView, name='IncidentDetailsRetrieveView'),
]
