from django.shortcuts import render, redirect
from apps.users.forms import LoginForms, RegisterForms

from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
  form = LoginForms()

  if request.method == 'POST':
     form = LoginForms(request.POST)

     if form.is_valid():
        # Variables
        login_name = form['login_name'].value()
        password = form['password'].value()

        user = auth.authenticate(
           request,
           username = login_name,
           password = password
        )

        if user is not None:
           auth.login(request, user)
           messages.success(request, 'Logged Successfully')
           return redirect('home')
        else:
           messages.error(request, 'Login Failed, check your credentials')
           return redirect('login')

  return render(request, "users/login.html", {"form": form})

def register(request):
    form = RegisterForms()

    if request.method == 'POST':
       form = RegisterForms(request.POST)

       if form.is_valid():

          # Variables
          name = form['name'].value()
          email = form['email'].value()
          password = form['password'].value()
          password_confirm = form['confirm_password'].value()

          # Check if User already exists
          if User.objects.filter(username = name).exists():
            messages.error(request, 'Username already exists')
            return redirect('register') 

          user = User.objects.create_user(
             username= name,
             email=email,
             password=password,
          )

          user.save()
          messages.success(request, 'User Registered')
          return redirect('login')

    return render(request, "users/register.html", {"form": form})

def logout(request):
   auth.logout(request)
   messages.success(request, 'Logout successfully')
   return redirect('login')