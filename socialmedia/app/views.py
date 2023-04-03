from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
       username = request.POST['username']
       email = request.POST['email']
       pass1 = request.POST['pass1']
       password = request.POST['pass2']
       print(pass1)
       if pass1 == password:
         if User.objects.filter(email=email).exists():
             messages.info(request, 'Email already exists')
             return redirect('signup')
         elif User.objects.filter(username=username).exits:
             messages.info(request, 'Username already exists')
             return redirect('signup')
         else:
             user = User.objects.create_user(username=username, email=email, password=password)
             user.save()
       else:
          messages.info(request ,'Password did not match' )
          return redirect('signup')

    else:
     return render(request,'signup.html')

def login(request):
    return render(request,'login.html')