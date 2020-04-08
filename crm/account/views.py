from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user)
        return redirect('home/')
    return render(request, "account/login.html",{'form':form})

def home(request):
    return render(request,"account/base.html")

def logout_view(request):
    logout(request)
    return redirect('accountLogin')