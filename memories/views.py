from django.contrib.auth import logout
from django.shortcuts import redirect, render

from .models import MemoryModel
from .forms import MemoryForm


def delete_memory(request, memory_id):
    MemoryModel.objects.filter(pk=memory_id, user_id=request.user.id).delete()
    return redirect('home-page')


def post_memory(request):
    if request.method == 'POST':

        form = MemoryForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            return redirect('add-memory-page')
    else:
        return redirect('add-memory-page')
    return redirect('home-page')


def home_page(request):
    memories = MemoryModel.objects.filter(user_id=request.user.id).all()
    return render(request, "memories/home.html", {'memories': memories})


def add_memory_page(request):
    return render(request, "memories/add-memory.html")


def logout_view(request):
    logout(request)
    return redirect('home-page')
