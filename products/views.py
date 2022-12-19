from django.shortcuts import render
from .models import Book
from api.serializers import *
from rest_framework import generics
from .utils import *


def Book(request):
    books, search_query = searchBooks(request)
    context = {'search_query': search_query}


