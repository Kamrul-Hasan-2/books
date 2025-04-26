from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'library_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('category/<slug:category_slug>/', views.category_books, name='category_books'),
    path('author/<int:author_id>/', views.author_books, name='author_books'),
    
    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='library_app/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='library_app:home'), name='logout'),
    path('accounts/profile/', views.user_profile, name='user_profile'),
    path('accounts/register/', views.register, name='register'),
]