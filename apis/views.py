# APIView class
from rest_framework.views import APIView

# Imports response object from API View
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is Similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]
        # Use a dictionary to format a return
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
