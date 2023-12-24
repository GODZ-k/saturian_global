from django.shortcuts import render
from core.models import *
# Create your views here.

def home(request):
    # service card
    services_card=services()
    data={
        **services_card,
    }
    return render(request, 'index.html',data)


def About(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contactus.html')


def Services(request):
    services_card=services()
    data={
        **services_card
    }
    return render(request, 'services.html',data)

def service_details(request):
    return render(request, 'service_detail.html')


def popular_services(request):
    return render(request, 'popular_service.html')


# service card
def services():
    card= service_card.objects.all()
    return {
        'item': card,
    }



def detail(request):
    items=product.objects.all()
    if request.method == 'GET':
        category_name=request.GET.get("category",'')
        if category_name:
            items=product.objects.filter(categories__name=category_name)

    data={
        "items": items,
        "category_name": category_name,
    }
    return render(request, 'details.html',data)