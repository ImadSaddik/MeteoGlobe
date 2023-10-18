from django.urls import path

from . import views

urlpatterns = [
    path('get_data/', views.getData.as_view(), name='get_data'),
]