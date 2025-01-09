

Here are 5 simple Django assignments related to models and migrations:

### 1. **Create a Simple Blog Application**
   - Create a model for `Post` with the following fields:
     - `title` (CharField)
     - `content` (TextField)
     - `published_date` (DateTimeField)
     - `author` (ForeignKey to a User model)
   - Create a migration and apply it to the database.

### 2. **E-commerce Product Catalog**
   - Create a `Product` model with these fields:
     - `name` (CharField)
     - `description` (TextField)
     - `price` (DecimalField)
     - `stock_quantity` (IntegerField)
     - `created_at` (DateTimeField)
   - Add a migration and apply it.

### 3. **Library Management System**
   - Create a `Book` model with the following fields:
     - `title` (CharField)
     - `author` (CharField)
     - `publication_date` (DateField)
     - `isbn` (CharField)
   - Add a `Member` model with:
     - `name` (CharField)
     - `email` (EmailField)
     - `membership_date` (DateField)
   - Define a ForeignKey relationship between `Book` and `Member` to represent which member has borrowed a book.
   - Add migrations and apply them.

### 4. **Simple To-Do List**
   - Create a model `Task` with the following fields:
     - `title` (CharField)
     - `description` (TextField)
     - `due_date` (DateField)
     - `status` (BooleanField, representing completed/incomplete)
   - Create migrations and apply them.

### 5. **User Profile**
   - Create a `Profile` model with the following fields:
     - `user` (OneToOneField linking to Django’s `User` model)
     - `phone_number` (CharField)
     - `address` (TextField)
   - Add migrations and apply them.

These assignments will help you practice creating models, defining fields, and handling migrations.