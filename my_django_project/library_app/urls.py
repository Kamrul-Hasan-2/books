from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('category/<slug:category_slug>/', views.category_books, name='category_books'),
    path('author/<int:author_id>/', views.author_books, name='author_books'),
]