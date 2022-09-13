from django.urls import path
from e_commerce.api.hola_mundo import *
from e_commerce.api.marvel_api_views import *

urlpatterns = [
    path('hola-mundo/',hola-mundo),
    path('request-data/',return_request_data),
    path('get_comics/',get_comics),
    path('purchased_item/',purchased_item),
]
 