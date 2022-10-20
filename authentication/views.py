import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def join(request):
    if request.method == 'POST':
        username = request.POST['usern']
        password = request.POST['pssw']
        useremail = request.POST['email']

        myuser = User.objects.create_user(username, useremail, password)
        myuser.is_active = 0

        myuser.save()

        messages.success(request, "Thank you! We will get back to you soon!")

        return redirect('home')

        messages.success(request, "Thank you! We will get back to you soon!")

    return render(request, "authentication/join.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            usrname = user.get_username
            return render(request, "authentication/index.html", {'usrname': usrname})

        else:
            messages.error(request, "Account not activated or no account with that username/password.")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect('home')
