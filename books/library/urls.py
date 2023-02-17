from django.urls import include, path
from .views import *


urlpatterns = [
    path('api/country', CountryCreate.as_view(), name='create-country'),
    path('api/country', CountryList.as_view()),
    path('api/country/<int:pk>', CountryDetail.as_view(), name='retrieve-country'),
    path('api/country/<int:pk>/', CountryUpdate.as_view(), name='update-country'),
    path('api/country/<int:pk>/', CountryDelete.as_view(), name='delete-country')
]
