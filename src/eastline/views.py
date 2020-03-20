from django.shortcuts import render,redirect
from .forms import SignUpForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.shortcuts import HttpResponse, HttpResponseRedirect
import socket
myhostname = socket.gethostname()
myhostip = socket.gethostbyname(myhostname)

def home_page(request):
    title = "Eastline | Welcome "
    template = "home.html"
    form  = SignUpForm(request.POST or None)
    context = {"title": title, "form": form}
    if form.is_valid():
        form.save()
    return render(request, template, context)

def sign_up_form(request):
    title = "Eastline | Sign Up"
    template = "signup.html"
    form = SignUpForm(request.POST or None)
    context  = {"title": title, "form": form}
    if form.is_valid():
        form.save()
        messages.info(request, "User has been successfully created")
    return render(request, template, context)
    

def log_in_form(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def log_out(request):
    auth.logout(request)
    return redirect('/')