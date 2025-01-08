

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



Here are 5 challenging Django assignments related to models, migrations, and advanced concepts:

---

### 1. **Blog with Categories and Tags**
   - Extend the blog application:
     - Create a `Category` model with:
       - `name` (CharField)
       - `slug` (SlugField)
     - Create a `Tag` model with:
       - `name` (CharField)
       - `slug` (SlugField)
     - Update the `Post` model to include:
       - `categories` (ManyToManyField linked to `Category`)
       - `tags` (ManyToManyField linked to `Tag`)
   - Add a custom manager to filter posts published in the last 30 days.
   - Add migrations and ensure data integrity.

---

### 2. **Order Management System**
   - Design models for an order management system:
     - `Customer` model:
       - `name` (CharField)
       - `email` (EmailField)
       - `phone` (CharField)
     - `Order` model:
       - `order_date` (DateTimeField)
       - `customer` (ForeignKey linked to `Customer`)
       - `total_amount` (DecimalField)
     - `OrderItem` model:
       - `order` (ForeignKey linked to `Order`)
       - `product_name` (CharField)
       - `price` (DecimalField)
       - `quantity` (IntegerField)
   - Use `signals` to automatically calculate and update the `total_amount` field in the `Order` model whenever an `OrderItem` is added or updated.
   - Create migrations and apply them.

---

### 3. **Advanced Library System**
   - Extend the library management system:
     - Add a `Publisher` model with:
       - `name` (CharField)
       - `address` (TextField)
       - `website` (URLField)
     - Update the `Book` model to include:
       - `publisher` (ForeignKey linked to `Publisher`)
       - `copies_available` (IntegerField)
     - Implement a `ManyToManyField` between `Book` and `Member` to track borrowing history with an intermediary model that includes:
       - `borrowed_date` (DateField)
       - `returned_date` (DateField)
   - Add a method in the `Book` model to check if a book is currently available.
   - Apply migrations and test your models.

---

### 4. **Polls Application with Results**
   - Create models for a polls application:
     - `Poll` model:
       - `question` (CharField)
       - `created_date` (DateTimeField)
     - `Choice` model:
       - `poll` (ForeignKey linked to `Poll`)
       - `choice_text` (CharField)
       - `votes` (IntegerField, default=0)
     - `Result` model:
       - `poll` (OneToOneField linked to `Poll`)
       - `winner_choice` (ForeignKey linked to `Choice`)
       - `total_votes` (IntegerField)
   - Use a `signal` to update the `Result` model when a poll’s choices are voted on.
   - Add migrations and test the logic.

---

### 5. **E-commerce with Discount System**
   - Extend the product catalog:
     - Add a `Coupon` model with:
       - `code` (CharField)
       - `discount_percent` (IntegerField)
       - `valid_from` (DateField)
       - `valid_to` (DateField)
     - Add a `DiscountedPrice` method in the `Product` model that applies a given coupon code and returns the discounted price.
     - Create a `Cart` model:
       - `user` (ForeignKey to `User`)
       - `products` (ManyToManyField to `Product` with an intermediary model to store quantity)
     - Add a method to calculate the cart total with applied discounts.
   - Ensure all migrations are created and applied.

---

These assignments will challenge you with **relationships**, **custom managers**, **signals**, and **complex queries**, deepening your understanding of Django's ORM.