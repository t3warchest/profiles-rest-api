from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, delete)',
            'Is Similar to a traditional Django View',
            'Gives you the most control over your application  logic ',
            'Mapped to url manually',
        ]
        return Response({'message':'hello' , "an_apiview":an_apiview})
    
    def post(self, request):
        """Create Hellow message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})  
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    
    def put(self, request, pk=None):
        """Handle Updating an object"""
        return Response({"methos":'PUT'})
    
    def patch(self, request, pk=None):
        """Handle Partial Updating an object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})