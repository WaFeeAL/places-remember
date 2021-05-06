from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MemoryModel
from .serializers import MemorySerializer


def delete_memory(request, memory_id):
    MemoryModel.objects.filter(pk=memory_id).delete()
    return redirect('home-page')


@api_view(['GET', 'POST'])
def memory_list(request):
    if request.method == 'GET':
        friends = MemoryModel.objects.all()
        serializer = MemorySerializer(friends, many=True)
        # return serializer.data
        return Response({"results": serializer.data})
    elif request.method == 'POST':
        print(request.data)
        serializer = MemorySerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return redirect('home-page')

#
# @api_view(['POST'])
# def memory_detail(request):
#     if request.method == 'POST':
#         print(request.data)
#         serializer = MemorySerializer(data=request.data)
#
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()


@api_view(['GET', 'PUT', 'DELETE'])
def memory_detail(request, memory_id):
    if request.method == 'GET':
        friend = get_object_or_404(MemoryModel, pk=memory_id)
        serializer = MemorySerializer(friend)

        return serializer.data
    # elif request.method == 'POST':
    #     print(request.data)
    #     serializer = MemorySerializer(data=request.data)
    #
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         # return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        friend = get_object_or_404(MemoryModel, pk=memory_id)
        serializer = MemorySerializer(friend, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        friend = get_object_or_404(MemoryModel, pk=memory_id)
        friend.delete()
        # return Response({"message": f"Friend with id {friend_id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)
