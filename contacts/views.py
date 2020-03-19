from django.shortcuts import render , redirect
from django.contrib import messages , auth
from .models import Contact
from django.core.mail import send_mail

def contact(request) :
    global listing_id
    if request.method == 'POST' :
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['email']

        if request.user.is_authenticated :
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id , user_id=user_id)
            if has_contacted:
                messages.error(request, "Your request is already been submitted")
                return redirect('/listings/' + listing_id)
        contact = Contact(listing=listing , listing_id=listing_id , name=name , email=email , message=message ,
                          phone=phone ,
                          user_id=user_id)
        contact.save()

        send_mail(
                    'Subject here' ,
                    'Here is the message.' + listing +'. sign in to admin panel to more information' ,
                    'from@example.com' ,
                    ['to@example.com'] ,
                    fail_silently=False ,
                       )
        messages.success(request , "Your request has been submit ,Realtor contact you soon")
        return redirect('/listings/' + listing_id)
# Create your views here.
