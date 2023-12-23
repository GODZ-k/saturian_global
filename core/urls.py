
from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("About/", About,name="about"),
    path("Contact/",contact,name="contact"),
    path('Services/',services,name="services"),
    path('Service_detail/',service_details,name="service_detail"),
    path('Popular_services/',popular_services,name="popular_service")
]
