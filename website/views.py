import json
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse


def home(request):
    context ={}
    return render(request, 'home.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_phone = request.POST.get('message-phone')
        message_email = request.POST.get('message-email')
        message_subject = request.POST.get('message-subject')
        message = request.POST.get('message')

        messageNote = 'Client Name: ' + message_name + ';  Client Phone#: ' + message_phone + ';  Email: ' + \
            message_email + ';  Messages: ' + message

        # send an email
        send_mail(
            'Quote or Message From ' + message_name + ': ' + message_subject,  # subject
            messageNote,  # message
            message_email,  
            ['youremail@email.com'],  # to email
            fail_silently=False,
        )
        print(message_email)

        context = {'message_name': message_name}
    else:
        context = {}
    return render(request, 'contact.html', context)


def payment(request):

    if request.method == "POST":
        payment_name = request.POST.get('payment-name')
        payment_email = request.POST.get('payment-email')
        payment_amount = request.POST.get('payment-amount')
        payment_phone = request.POST.get('payment-phone')
        payment_invoice = request.POST.get('payment-invoice')
        payment_message = request.POST.get('payment-message')

        context = {'payment_name': payment_name,
                   'payment_amount': payment_amount, 'payment_email': payment_email, 'payment_phone': payment_phone, 'payment_invoice': payment_invoice, 'payment_message': payment_message}
        return render(request, 'payment.html', context)
    else:
        return render(request, 'payment.html')


def processPayment(request):
    data = json.loads(request.body)
    messageNote = 'Client Name: ' + \
        data['form']['name'] + '; Payment Amount: $' + data['form']['amount'] + '; Client email: ' + \
        data['form']['email'] + '; Client phone#: '+data['form']['phone'] + \
        '; Client invoice#: '+data['form']['invoice'] + \
        '; Payment Message: '+data['form']['message']

    send_mail(
        'Payment Received From ' + data['form']['name'] +
        '; Amount: $' + data['form']['amount'],  # subject
        messageNote,  # message
        'tarowebsitedesign@gmail.com',  # from email
        ['tarowebsitedesign@gmail.com'],  # to email
        fail_silently=False,
    )

    return JsonResponse('Payment confirmation email send...', safe=False)
