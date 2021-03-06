from django.shortcuts import render
# from django.http import JsonResponse # We will be using the rest framework instead
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GdpData
from .serializers import GdpSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/gdp/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of gdp'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getData(request):
    gdpData = GdpData.objects.all()
    serializer = GdpSerializer(gdpData, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDataSingle(request, pk):
    gdpData = GdpData.objects.get(id=pk)
    serializer = GdpSerializer(gdpData, many=True)
    return Response(serializer.data)