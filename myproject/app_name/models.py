from django.db import models
from datetime import timedelta
from django.utils.timezone import now

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
# book = Book(title="Django Basics", author="John Doe", published_date="2023-01-01", price=19.99)
# book.save()

# books = Book.objects.all()


# 1. Create a Simple Blog Application
#       Create a model for Post with the following fields:
#       title (CharField)
#       content (TextField)
#       published_date (DateTimeField)
#       author (ForeignKey to a User model)
#       Create a migration and apply it to the database.


# 1. Blog with Categories and Tags
#         Extend the blog application:
#         Create a Category model with:
#         name (CharField)
#         slug (SlugField)
#         Create a Tag model with:
#         name (CharField)
#         slug (SlugField)
#         Update the Post model to include:
#         categories (ManyToManyField linked to Category)
#         tags (ManyToManyField linked to Tag)
#         Add a custom manager to filter posts published in the last 30 days.
#         Add migrations and ensure data integrity.

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    
class Tag(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()

class User(models.Model):
    name = models.CharField(max_length=45)
    
class PostManager(models.Manager):
    def recent_posts(self):
        return self.filter(created_at__gte=now() - timedelta(days=30))
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,related_name="post")
    tag = models.ManyToManyField(Tag,related_name="post")
    
    object = PostManager()
    
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
    
# 4. Simple To-Do List
#         Create a model Task with the following fields:
#         title (CharField)
#         description (TextField)
#         due_date (DateField)
#         status (BooleanField, representing completed/incomplete)
#         Create migrations and apply them.

class Task(models.Model):
    status_choices=[
        (True,"complete"),
        (False,"incomplete")
    ]
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    due_date = models.DateField()
    status = models.BooleanField(choices=status_choices,default=False)
    
# 5. User Profile
#         Create a Profile model with the following fields:
#         user (OneToOneField linking to Django’s User model)
#         phone_number (CharField)
#         address (TextField)
#         Add migrations and apply them.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    