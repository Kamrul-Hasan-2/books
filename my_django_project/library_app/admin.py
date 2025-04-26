from django.contrib import admin
from .models import Book, Author, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'author__name', 'description')