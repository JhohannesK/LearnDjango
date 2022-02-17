from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.template import RequestContext

def index(request):
      return render(request, 'accounts/home.html')

def LogIn(request):
      if request.method == 'POST':
                  username = request.POST.get('username')
                  password = request.POST.get('password')

                  user = authenticate(username=username, password=password)
                  
                  if user is not None:
                        login(request, user)
                        return redirect(index)
                  else:
                        messages.error(request, "Invalid username or password")
      else:
            print('dont know')
      
      return render(request, 'accounts/login.html')