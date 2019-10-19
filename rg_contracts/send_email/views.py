from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def contact(request):
    subject = request.POST.get('subject')
    customer_email = request.POST.get('email')
    from_email = 'darrenlallybusiness@hotmail.com'
    message1 = request.POST.get('message')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')

    firstname1 = str(firstname)
    lastname1 = str(lastname)
    customer_email1 = str(customer_email)
    message = 'Client Name: ' + firstname1 + ' ' + lastname1 + '\n Message: ' + str(message1) + '\n' + 'Client Email: ' + customer_email1
    if request.method == 'POST':
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['darrenlallybusiness@hotmail.com'], fail_silently= False)
            except BadHeaderError:
                return HttpResponse('Invalid Header found')
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('ENSURE ALL FIELDS ARE FILLED')

        
             
    return render(request, 'send_email/contact.html')