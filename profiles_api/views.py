from rest_framework.views import APIView
from rest_framework.response import Response


class HellowApiView(APIView):
    """Test Api view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most ocntrol over you application logic',
            'Is mapped manualy to URLs',
        ]

        return Response({'message':'AOA', 'an_apiview': an_apiview})