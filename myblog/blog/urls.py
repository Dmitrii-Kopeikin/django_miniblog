from django.urls import path
from . import views


urlpatterns = [path('', views.PublicationView.as_view())]
