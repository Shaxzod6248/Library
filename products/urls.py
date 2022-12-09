from django.urls import path
from .views import *


urlpatterns = [
    path('searched_books', search_book, name = 'book_search'),
]