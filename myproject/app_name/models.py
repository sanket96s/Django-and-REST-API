from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
book = Book(title="Django Basics", author="John Doe", published_date="2023-01-01", price=19.99)
book.save()

books = Book.objects.all()