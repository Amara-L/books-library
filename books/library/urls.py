from django.urls import include, path
from .views import *


urlpatterns = [
    path('api/country', country_view),
    path('api/author', author_view),
    path('api/publishing', publishing_view),
    path('api/book', book_view),
]
