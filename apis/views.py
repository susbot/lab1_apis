# APIView class
from rest_framework.views import APIView

# Imports response object from API View
from rest_framework.response import Response

# Status codes from DRF list for return responses
from rest_framework import status

# Viewsets from the REST framework
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


# Serializers module from serializers.py
from apis import serializers
from apis import models
from apis import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'automatically maps to URLS using routers',
            'provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(selfs, request, pk=None):
        """Handle updating an Object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial updates on object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an Object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSets(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # How the user will authenticate
    authentication_classes = (TokenAuthentication,)
    # Permissions to do something
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    # Tells the filter backend which fields are searchable
    search_fields = ('name', 'email')


# User login API VIEW
class UserLoginApiView(ObtainAuthToken):
    """Handling creating User auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Basic model view set for CRUD
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles CRUD Profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        # Handy feature to over right create objects of the ViewSet
        serializer.save(user_profile=self.request.user)
