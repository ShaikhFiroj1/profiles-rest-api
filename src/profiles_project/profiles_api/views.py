from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.
class HelloAPIView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """REturn the list of feature of API view"""

        an_apiview = [
            'usse htttp method as funtion(post,get,put,patch)',
            'It is similar to traditional django view',
            'gives u the most control over logic',
            'Is mapped manualy to URLs'
        ]
        return Response({'messages': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create an hello messages with our name"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles the updating of object"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch request, only update the fields provided in request(partial update)"""

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Delete the object"""

        return Response({'method':'delete'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ return the hello message"""

        a_viewset = [
            'Uses action (list, create, update, partial_update)',
            'Automatically maps to URL using router',
            'Provide more funtionality for less code'
        ]

        return Response({'message': 'Hello','a_viewset': a_viewset})

    def create(self,request):
        """create new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        """handles getting object by its ID"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """handles updating object"""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """handles updating part of an object"""

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """handles removing an object"""

        return Response({'http_method':'DELETE'})
