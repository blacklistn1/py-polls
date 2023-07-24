from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ViewSet

from . import serializers


# Create your views here.
class HelloApiView(APIView):
    """Returns API View features"""
    serializer_class = serializers.HelloSerializer

    def get(self, request):
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(ViewSet):
    """Provide basic customizations for basic operations"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, delete)',
            'Automatically maps to URLs using Routers',
            'Provides more functionalities',
        ]

        return Response({'message': 'Hello from ViewSet', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Welcome {name} to Hello View set'
            return Response({'message': message})
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting a single object by ID"""
        return Response({'method': 'GET', 'id': pk})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT', 'id': pk})

    def partial_update(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'request': 'PATCH', 'id': pk})

    def destroy(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'DELETE', 'id': pk})
