from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def profile(request):
    current_user = User.objects.all()
    print(current_user)
    return render(request, "users/profile.html", {"ED": "ME"})


def register(request):
    return render(request, "users/register.html", {"ED": "ME"})


def login(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "users/login.html", {"error": "Wrong username or password!"})
    return render(request, "users/login.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
