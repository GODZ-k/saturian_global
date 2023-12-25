from django.shortcuts import render,redirect
from core.models import *
from django.core.mail import EmailMessage
from saturianglobal import settings
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    #form save
    form(request)
    # service card
    services_card=services()
    data={
        **services_card,
    }
    return render(request, 'index.html',data)


def About(request):
    return render(request, 'About.html')

def contact(request):
    # form save
    form(request)
    return render(request, 'Contactus.html')


def Services(request):
    services_card=services()
    data={
        **services_card
    }
    return render(request, 'services.html',data)

def service_details(request):
    # form save
    form(request)

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

    # enquiry form
    enquiry_form(request)
    items=product.objects.all()
    # if request.method == 'GET':
    category_name=request.GET.get("category",'')
    if category_name:
            items=product.objects.filter(categories__name=category_name)

    data={
        "items": items,
        "filter": category_name,
    }
    return render(request, 'details.html',data)



# form submit


def form(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact_=request.POST.get("contact")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        save_form=Contact(name=name, email=email, contact=contact_, subject=subject,message=message)
        save_form.save()

        # send to user
        send_greeting(name,email)

        # send to admin
        send_to_boss(name,email,contact_,subject,message)
        return redirect('/')


def send_greeting(name,email):
    subject="Welcome to Saturian Global - Thanks for contacting us"
    message=render_to_string("greeting.html",{
            "name":name,
        })
    send_mail=EmailMessage(subject,message,settings.EMAIL_HOST_USER,[email])
    send_mail.fail_silently=True
    send_mail.send()


def send_to_boss(name,email,contact_,subject,message):
    subject="User information"
    message=render_to_string("user_data.html",{
            "name":name,
            "subject":subject,
            "email":email,
            "contact":contact_,
            "message":message

        })
    send_mail=EmailMessage(subject,message,settings.EMAIL_HOST_USER,["saturianglobal@gmail.com"])
    send_mail.fail_silently=True
    send_mail.send()



# enquiry form regarding product

def enquiry_form(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact_=request.POST.get('contact')
        period=request.POST.get('period')
        Quantity=request.POST.get('quantity')
        product=request.POST.get('product')
        message=request.POST.get('message')
        save_form=Product_form(name=name, email=email, contact=contact_, period=period,Quantity=Quantity,product=product,message=message)
        save_form.save()

        # send to user
        send_to_user(name,product,email)

        # send to admin
        send_to_admin(name,email,contact_,period,Quantity,product,message)
        return redirect("/")

def send_to_user(name,product,email):
    subject="Welcome to Saturian Global - Thanks for contacting us"
    message=render_to_string("welcome.html",{
            "name":name,
            "product":product,
        })
    send_mail=EmailMessage(subject,message,settings.EMAIL_HOST_USER,[email])
    send_mail.fail_silently=True
    send_mail.send()


def send_to_admin(name,email,contact_,period,Quantity,product,message):
    subject="User information"
    message=render_to_string("user_info.html",{
            "name":name,
            "product":product,
            "email":email,
            "contact":contact_,
            "period":period,
            "Quantity":Quantity,
            "message":message

        })
    send_mail=EmailMessage(subject,message,settings.EMAIL_HOST_USER,["saturianglobal@gmail.com"])
    send_mail.fail_silently=True
    send_mail.send()
