from django.urls import path
from .views import RegistrationApiView
urlpatterns = [
    path('',RegistrationApiView.as_view())
]
