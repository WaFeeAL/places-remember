from django.shortcuts import redirect
from django.views.decorators.http import require_GET, require_POST

from .models import MemoryModel
from .serializers import MemorySerializer


def delete_memory(request, memory_id):
    MemoryModel.objects.filter(pk=memory_id, user_id=request.user.id).delete()
    return redirect('home-page')


@require_GET
def get_memory_list(request):
    if request.method == 'GET':
        friends = MemoryModel.objects.filter(user_id=request.user.id).all()
        serializer = MemorySerializer(friends, many=True)

        return serializer.data


@require_GET
def get_memory(request, memory_id):
    if request.method == 'GET':
        # friend = get_object_or_404(MemoryModel, pk=memory_id)
        friend = MemoryModel.objects.filter(pk=memory_id, user_id=request.user.id).all()
        serializer = MemorySerializer(friend)

        return serializer.data


@require_POST
def post_memory(request):
    if request.method == 'POST':
        serializer = MemorySerializer(data=request.POST)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return redirect('home-page')
