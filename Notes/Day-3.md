

Here's a detailed breakdown for studying **Django Models and Databases** and **Creating and Applying Migrations**. This will help you cover the topic thoroughly over 5 hours.

---

### **1. Introduction to Django Models (1 hour)**  
1. **What are Models?**  
   - Models are Python classes used to define the structure of your database tables.  
   - Located in the `models.py` file of a Django app.  
   - A model is mapped to a single table in the database.  

2. **Core Concepts:**  
   - Fields: Define the columns of the table (e.g., `CharField`, `IntegerField`, `DateField`).  
   - Methods: Define custom behavior for your model objects.  
   - Meta Class: Provides metadata options (e.g., ordering, db_table).  

3. **Example of a Basic Model:**  
   ```python
   from django.db import models

   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.CharField(max_length=50)
       published_date = models.DateField()
       price = models.DecimalField(max_digits=10, decimal_places=2)
   ```

4. **Key Field Types:**  
   - `CharField`: Variable-length text (requires `max_length`).  
   - `IntegerField`: Integer numbers.  
   - `FloatField`: Floating-point numbers.  
   - `BooleanField`: True/False values.  
   - `DateField` and `DateTimeField`: Dates and timestamps.  
   - `ForeignKey`: For relationships (one-to-many).  
   - `ManyToManyField`: Many-to-many relationships.  

5. **Model Instance Operations:**  
   - Creating an instance:  
     ```python
     book = Book(title="Django Basics", author="John Doe", published_date="2023-01-01", price=19.99)
     book.save()
     ```
   - Querying instances:  
     ```python
     books = Book.objects.all()  # Retrieve all books
     ```

---

### **2. Connecting Models to a Database (1 hour)**  
1. **Setting up the Database:**  
   - Default is SQLite (defined in `settings.py`).  
   - Locate the database settings in `settings.py`:  
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
     ```
   - Replace `sqlite3` with other database backends if using MySQL, PostgreSQL, etc.

2. **Registering Models in `admin.py`:**  
   - Enable model visibility in the Django admin interface.  
   - Example:  
     ```python
     from django.contrib import admin
     from .models import Book

     admin.site.register(Book)
     ```

3. **Interacting with the Database:**  
   - Run `python manage.py dbshell` to interact directly with the database (for supported backends).  

---

### **3. Migrations in Django (2 hours)**  
1. **What are Migrations?**  
   - Migrations are Python scripts used to propagate changes made to your models into the database schema.  

2. **Creating Migrations:**  
   - After defining or modifying models, create migrations using:  
     ```bash
     python manage.py makemigrations
     ```
   - This generates migration files in the `migrations` folder of your app.  

3. **Applying Migrations:**  
   - Apply the generated migrations to the database using:  
     ```bash
     python manage.py migrate
     ```

4. **Migration File Structure:**  
   - Each migration file contains instructions for altering the database schema.  
   - Example of a migration file:  
     ```python
     from django.db import migrations, models

     class Migration(migrations.Migration):
         dependencies = [
             ('app_name', '0001_initial'),
         ]

         operations = [
             migrations.AddField(
                 model_name='book',
                 name='genre',
                 field=models.CharField(max_length=50, default='Fiction'),
             ),
         ]
     ```

5. **Understanding Migration Commands:**  
   - `makemigrations`: Detects changes in models and prepares migration scripts.  
   - `migrate`: Applies migrations to the database.  
   - `sqlmigrate`: Views SQL commands for a migration.  
     ```bash
     python manage.py sqlmigrate app_name 0001
     ```
   - `showmigrations`: Lists all migrations and their statuses.  
     ```bash
     python manage.py showmigrations
     ```

---

### **4. Hands-On Practice and Troubleshooting (1 hour)**  
1. **Practice Model Creation:**  
   - Create models for different scenarios (e.g., e-commerce products, user profiles).  
   - Define relationships between models using `ForeignKey` and `ManyToManyField`.  

2. **Run Queries in the Shell:**  
   - Launch the Django shell:  
     ```bash
     python manage.py shell
     ```
   - Perform CRUD operations on your models.  

3. **Common Migration Issues and Fixes:**  
   - If migrations aren't detecting changes, ensure `makemigrations` is run in the correct app.  
   - Delete and recreate migrations only if absolutely necessary (use caution).  

4. **Database Constraints and Indexes:**  
   - Add constraints like `unique=True` in fields.  
   - Use `Meta` options for indexes:  
     ```python
     class Meta:
         indexes = [
             models.Index(fields=['title']),
         ]
     ```

---

### **5. Assignment (Hands-On Practice)**  
Spend the last hour on the following:  

1. **Create a New App:**  
   - Add an app to your project:  
     ```bash
     python manage.py startapp library
     ```

2. **Define Models in `models.py`:**  
   ```python
   class Author(models.Model):
       name = models.CharField(max_length=100)
       birth_date = models.DateField()

   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.ForeignKey(Author, on_delete=models.CASCADE)
       published_date = models.DateField()
   ```

3. **Create and Apply Migrations:**  
   - Generate and apply migrations.  

4. **Add Data Using the Shell:**  
   - Add sample data for authors and books.  
   - Query and display the data in the shell.  

5. **Register Models in Admin:**  
   - Verify that the models appear in the Django admin panel.  

---

By the end of this 5-hour session, you should have a clear understanding of how to work with Django models and migrations, and you'll have practical experience building and interacting with a database in Django.