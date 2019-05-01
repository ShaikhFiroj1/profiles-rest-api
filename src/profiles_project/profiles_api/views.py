from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """REturn the list of feature of API view"""

        an_apiview = [
            'usse htttp method as funtion(post,get,put,patch)',
            'It is similar to traditional django view',
            'gives u the most control over logic',
            'Is mapped manualy to URLs'
        ]
        return Response({'messages': 'Hello!', 'an_apiview': an_apiview})
