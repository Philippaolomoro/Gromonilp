from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Clients
# tryout added
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from onboarding_form.serializers import ClientsSerializer

from .serializers import *


# Create your views here.

# @api_view(['GET', 'POST', 'DELETE'])
# def onboarding_form_list(request):
#     if request.method == 'GET':
#         data = Clients.objects.all()

#         data_serializer = ClientsSerializer(
#             data, many=True)

#         return JsonResponse(data_serializer.data, safe=False)


# @api_view(['GET', 'PUT', 'DELETE'])
# def onboarding_form_detail(request, pk):
#     try:
#         onboarding_form = Clients.objects.get(pk=pk)
#     except Clients.DoesNotExist:
#         return JsonResponse({'message': 'The Client does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def onboarding_form_list(request):
    if request.method == 'GET':
        data = Clients.objects.all()

        serializer = ClientsSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def onboarding_form_detail(request, pk):
    try:
        onboarding_form = Clients.objects.get(pk=pk)
    except Clients.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ClientsSerializer(
            onboarding_form, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        onboarding_form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
