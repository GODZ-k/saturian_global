from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contactus.html')


def services(request):
    return render(request, 'services.html')

def service_details(request):
    return render(request, 'service_detail.html')


def popular_services(request):
    return render(request, 'popular_service.html')