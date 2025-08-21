from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    # Clients
    path("clients/", views.client_list, name="client_list"),
    path("clients/add/", views.client_create, name="client_create"),
    path("clients/<int:pk>/edit/", views.client_update, name="client_update"),
    path("clients/<int:pk>/delete/", views.client_delete, name="client_delete"),

    # Jobs
    path("jobs/", views.job_list, name="job_list"),
    path("jobs/add/", views.job_create, name="job_create"),
    path("jobs/<int:pk>/edit/", views.job_update, name="job_update"),
    path("jobs/<int:pk>/delete/", views.job_delete, name="job_delete"),
]
