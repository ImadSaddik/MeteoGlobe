from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Meteorite
from .serializers import MeteoriteSerializer


class getData(APIView):
    def get(self, request):
        data = Meteorite.objects.all()
        serializer = MeteoriteSerializer(data, many=True)
        
        return Response(serializer.data)

