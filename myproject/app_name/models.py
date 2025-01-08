from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
book = Book(title="Django Basics", author="John Doe", published_date="2023-01-01", price=19.99)
book.save()

books = Book.objects.all()


# 1. Create a Simple Blog Application
#       Create a model for Post with the following fields:
#       title (CharField)
#       content (TextField)
#       published_date (DateTimeField)
#       author (ForeignKey to a User model)
#       Create a migration and apply it to the database.

class User(models.Model):
    name = models.CharField(max_length=45)
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
# 2. E-commerce Product Catalog
#         Create a Product model with these fields:
#         name (CharField)
#         description (TextField)
#         price (DecimalField)
#         stock_quantity (IntegerField)
#         created_at (DateTimeField)
#         Add a migration and apply it.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=100,decimal_places=2)
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    

# 3. Library Management System
#         Create a Book model with the following fields:
#         title (CharField)
#         author (CharField)
#         publication_date (DateField)
#         isbn (CharField)
#         Add a Member model with:
#         name (CharField)
#         email (EmailField)
#         membership_date (DateField)
#         Define a ForeignKey relationship between Book and Member to represent which member has borrowed a book.
#         Add migrations and apply them.

class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    membership_date = models.DateField()
    
    def __str__(self):
        return self.name

class Boook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    borrowed_by = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title