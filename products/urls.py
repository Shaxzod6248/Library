from django.urls import path
from .views import *


urlpatterns = [
    path('searchBooks/', searchBooks),
]