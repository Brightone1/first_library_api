from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    """show all books"""
    book_list = Book.objects.all()
    
    context = {'book_list':book_list}
    return render(request, 'books/book_list.html', context)