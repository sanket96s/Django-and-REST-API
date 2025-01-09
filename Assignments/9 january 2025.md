### 1. Create a Book model with the following fields:
  
  - title (CharField, max_length=100)
  - author (CharField, max_length=100)
  - published_date (DateField)
  - price (DecimalField, max_digits=10, decimal_places=2)
  - stock (IntegerField)

  Register the model in admin.py and customize it to include:

    - list_display: Show title, author, and price.
    - search_fields: Allow searching by title and author.
    - list_filter: Add a filter for published_date.

### 2: Inline Models

  Create the following models:

    - Order: Contains customer_name (CharField) and order_date (DateTimeField).

    - OrderItem: Contains order (ForeignKey  to Order), product (CharField), and quantity (IntegerField).
    
    - Register Order in the admin and use OrderItemInline to display related items inline.