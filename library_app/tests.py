from django.test import TestCase
from django.db import connection
from .models import Author, Category, Book

class ModelTests(TestCase):
    def setUp(self):
        # Create test data
        self.category = Category.objects.create(name="Fiction", slug="fiction")
        self.author = Author.objects.create(name="Test Author", bio="Test biography")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            category=self.category,
            description="Test description",
            is_featured=True
        )
    
    def test_category_model(self):
        """Test the Category model"""
        self.assertEqual(str(self.category), "Fiction")
        self.assertEqual(self.category.slug, "fiction")
    
    def test_author_model(self):
        """Test the Author model"""
        self.assertEqual(str(self.author), "Test Author")
        self.assertEqual(self.author.bio, "Test biography")
    
    def test_book_model(self):
        """Test the Book model"""
        self.assertEqual(str(self.book), "Test Book")
        self.assertEqual(self.book.author.name, "Test Author")
        self.assertEqual(self.book.category.name, "Fiction")
        self.assertTrue(self.book.is_featured)

class DatabaseTablesTest(TestCase):
    def test_tables_exist(self):
        """Test that the required database tables exist"""
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [table[0] for table in cursor.fetchall()]
            
        # Check that our model tables exist
        self.assertIn('library_app_author', tables)
        self.assertIn('library_app_category', tables)
        self.assertIn('library_app_book', tables)
