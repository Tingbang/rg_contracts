from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):
    return render(request, 'base_site/home.html')

def products(request):
    my_context={
        "range": 4
    }

    return render(request, 'base_site/products.html', my_context)

def contact(request):
    return render(request, 'base_site/contact.html')

def services(request):
    return render(request, 'base_site/services.html')

