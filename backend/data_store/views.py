from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Q

from .models import Meteorite
from .serializers import MeteoriteSerializer


class getData(APIView):
    def get(self, request):
        min_mass = request.GET.get('min_mass', -1)
        max_mass = request.GET.get('max_mass', -1)
        country = request.GET.get('country', '')
        discovery_year = request.GET.get('discovery_year', -1)
        discovery_type = request.GET.get('discovery_type', '')
        chemical_composition = request.GET.get('chemical_composition', '')
        
        data = Meteorite.objects.all()
        if min_mass != -1:
            data = data.filter(mass__gte=min_mass)

        if max_mass != -1:
            data = data.filter(mass__lte=max_mass)

        if country != '':
            data = data.filter(country__icontains=country)

        if discovery_year != -1:
            data = data.filter(year__icontains=discovery_year)
            
        if discovery_type != '':
            data = data.filter(discovery_type__icontains=discovery_type)
            
        if chemical_composition != '':
            data = data.filter(recorded_class__icontains=chemical_composition)
        
        serializer = MeteoriteSerializer(data, many=True)        
        return Response(serializer.data)
    
    
@api_view(['GET'])
def getCountryList(request):
    country_list = Meteorite.objects.values_list('country', flat=True).distinct()
    country_list = sorted(country_list)
    return Response(country_list)


@api_view(['GET'])
def getDiscoveryTypeList(request):
    discovery_type_list = Meteorite.objects.values_list('discovery_type', flat=True).distinct()
    return Response(discovery_type_list)


@api_view(['GET'])
def getChemicalCompositionList(request):
    chemical_composition_list = Meteorite.objects.values_list('recorded_class', flat=True).distinct()
    chemical_composition_list = sorted(chemical_composition_list)
    return Response(chemical_composition_list)
