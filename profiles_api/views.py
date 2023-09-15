from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """returns a list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, delete)',
            'Is Similar to a traditional Django View',
            'Gives you the most control over your application  logic ',
            'Mapped to url manually',
        ]
        return Response({'message':'hello' , "an_apiview":an_apiview})
