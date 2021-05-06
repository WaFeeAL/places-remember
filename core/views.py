from django.contrib.auth import logout
from django.shortcuts import render, redirect

from memories.models import MemoryModel


def home_page(request):
    print(request.user.id)
    memories = MemoryModel.objects.filter(user_id=request.user.id).all()
    print(memories)
    return render(request, "core/home.html", {'memories': memories})


def add_memory_page(request):
    return render(request, "core/add-memory.html")


def logout_view(request):
    logout(request)
    return redirect('home-page')
