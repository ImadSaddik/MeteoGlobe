from django.urls import path

from . import views

urlpatterns = [
    path('get_points_data/', views.getData.as_view(), name='get_data'),
    path('get_country_list/', views.getCountryList, name='get_country_list'),
    path('get_discovery_type_list/', views.getDiscoveryTypeList, name='get_discovery_type_list'),
    path('get_chemical_composition_list/', views.getChemicalCompositionList, name='get_chemical_composition_list'),
]