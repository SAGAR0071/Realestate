from django.shortcuts import render , redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

from contacts.models import Contact
def register(request) :
    if request.method == 'POST' :
        #Get form values
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        #check if password match
        if password==password2:
           if User.objects.filter(username=username).exists():
               messages.error(request,'that username is taken')
               return redirect('register')
           else:
               if User.objects.filter(email=email).exists():
                   messages.error(request , 'that email is being used')
                   return redirect('register'  )
               else:
                  user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                 #login After Register
                  #auth.login(request,user)
                  #messages.success(request,'You are Logged In')
                  #return redirect ( 'index')
                  user.save()
                  messages.success(request,'you are now registered and can log in')
                  return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else :
        return render(request , 'accounts/register.html')


def login(request) :
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request , user)
            messages.success(request  , 'You are Logged in')
            return redirect('dashboard')
        else:
            messages.error(request , "invalid Input")
            return redirect('login')
    else :
        return render(request , 'accounts/login.html')


def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        messages.success(request , "you are logged out")
    return redirect('index')


def dashboard(request) :
    user_contacts=Contact.objects.order_by('-contact_Date').filter(user_id=request.user.id)

    context = {
        'contacts' : user_contacts
          }
    return render(request , 'accounts/dashboard.html',context)

# Create your views here.
