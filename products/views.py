from django.shortcuts import render
from .models import Book


def search_book(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    return render(request, {'searched_books':searched_books})