from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Category, Author, UserProfile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

ROOT_URLCONF = 'library_app.urls'

def home(request):
    # Get books from the database
    featured_books = Book.objects.filter(is_featured=True)
    recent_books = Book.objects.all().order_by('-created_at')[:6]
    categories = Category.objects.all()
    
    context = {
        'featured_books': featured_books,
        'recent_books': recent_books,
        'categories': categories,
    }
    return render(request, 'library_app/home.html', context)

def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    
    # Handle search
    query = request.GET.get('q')
    if query:
        books = books.filter(title__icontains=query)
    
    context = {
        'books': books,
    }
    return render(request, 'library_app/book_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book,
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

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'অ্যাকাউন্ট সফলভাবে তৈরি হয়েছে! এখন আপনি লগইন করতে পারেন।')
            return redirect('library_app:login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'library_app/register.html', {'form': form})

@login_required
def user_profile(request):
    # Ensure the user has a profile
    try:
        profile = request.user.profile
    except:
        # Create a profile if it doesn't exist
        profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'আপনার প্রোফাইল আপডেট করা হয়েছে!')
            return redirect('library_app:user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)
    
    # Get user's recently visited books
    recent_books = Book.objects.all().order_by('-created_at')[:4]
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'recent_books': recent_books
    }
    return render(request, 'library_app/profile.html', context)
