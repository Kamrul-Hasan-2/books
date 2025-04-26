from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book, Category, Author

def home(request):
    featured_books = Book.objects.filter(is_featured=True)[:6]
    categories = Category.objects.all()
    recent_books = Book.objects.order_by('-created_at')[:6]
    
    context = {
        'featured_books': featured_books,
        'categories': categories,
        'recent_books': recent_books,
    }
    return render(request, 'library_app/home.html', context)

def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    # Filter by category if provided
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(description__icontains=query)
        )
    
    context = {
        'books': books,
        'categories': categories,
    }
    return render(request, 'library_app/book_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    related_books = Book.objects.filter(category=book.category).exclude(id=book.id)[:4]
    
    context = {
        'book': book,
        'related_books': related_books,
    }
    return render(request, 'library_app/book_detail.html', context)

def category_books(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    books = Book.objects.filter(category=category)
    
    context = {
        'category': category,
        'books': books,
    }
    return render(request, 'library_app/category_books.html', context)

def author_books(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)
    
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'library_app/author_books.html', context)