from django.contrib.auth import logout
from django.shortcuts import render, redirect


def home(request):
    return render(request, "core/home.html")


def logout_view(request):
    logout(request)
    return redirect('home-page')
