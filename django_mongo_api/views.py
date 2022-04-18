from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from django_mongo_api.models import Test
from django_mongo_api.serializers import TestSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def test_data(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse(data=data, status=status.HTTP_200_OK)
    return JsonResponse(
        {
            'message': 'test api working properly'
        },
        status = status.HTTP_200_OK
    )