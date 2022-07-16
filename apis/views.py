# APIView class
from rest_framework.views import APIView

# Imports response object from API View
from rest_framework.response import Response

# Status codes from DRF list for return responses
from rest_framework import status

# Serializers module from serializers.py
from apis import serializers


class HelloApiView(APIView):
    """Test API View"""
    # Set the serializer
    serializer_class = serializers.HelloSerializer

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

    def post(self, request):
        """Create a Hello message with our name"""
        # Retrieve the serializer and pass the data sent in the request
        # self.serializers_class retrieves configured serializer class for view
        serializer = self.serializer_class(data=request.data)

        # Validate serializer name is no longer than 10 char
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            # return response in a dictionary
            return Response({'message': message})
            # If input is not valid return a 400 response
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        # Defines a new method for PUT requests - update
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
