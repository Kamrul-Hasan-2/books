from django.contrib import admin
from .models import Author, Category, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'author', 'is_featured')
    search_fields = ('title', 'description', 'author__name')
    date_hierarchy = 'created_at'

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
