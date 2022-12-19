from .models import *
from django.db.models import Q


def searchBooks(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    books = Book.objects.distinct().filter(
        Q(title__icontains=search_query)
    )

    return books