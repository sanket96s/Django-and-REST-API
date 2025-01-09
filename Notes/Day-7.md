Here's a step-by-step guide for handling forms in Django, with proper file names and clear instructions:

---

### **Step 1: Create a Django Project and App**
1. Create a new Django project (if not already created):
   ```bash
   django-admin startproject myproject
   cd myproject
   ```
2. Create a new app for handling forms:
   ```bash
   python manage.py startapp forms_app
   ```
3. Add the app to `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       # other apps
       'forms_app',
   ]
   ```

---

### **Step 2: Define the Form**
**File:** `forms_app/forms.py`

Create a form using Django’s `forms` module:
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
```

---

### **Step 3: Set Up the View**
**File:** `forms_app/views.py`

Handle the form submission and render the form:
```python
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Example: Save to database or send an email
            return HttpResponse("Thank you for your message!")
    else:
        form = ContactForm()
    return render(request, 'forms_app/contact.html', {'form': form})
```

---

### **Step 4: Create the HTML Template**
**File:** `forms_app/templates/forms_app/contact.html`

Render the form and include the CSRF token:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

---

### **Step 5: Configure URLs**
1. **Project URLs:** `myproject/urls.py`
   Include the app's URLs in the project:
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('contact/', include('forms_app.urls')),  # Add this line
   ]
   ```

2. **App URLs:** `forms_app/urls.py`
   Define the app-specific URLs:
   ```python
   from django.urls import path
   from .views import contact_view

   urlpatterns = [
       path('', contact_view, name='contact'),
   ]
   ```

---

### **Step 6: Run the Server**
Start the development server:
```bash
python manage.py runserver
```

Access the form at: [http://127.0.0.1:8000/contact/](http://127.0.0.1:8000/contact/)

---

### **Summary of File Structure**
```plaintext
myproject/
│
├── forms_app/
│   ├── migrations/
│   ├── templates/
│   │   └── forms_app/
│   │       └── contact.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

### **Steps Recap**
1. Create a Django project and app.
2. Define the form in `forms.py`.
3. Create a view to handle the form submission (`views.py`).
4. Design the HTML template (`contact.html`).
5. Configure URLs for routing (`urls.py` in both the app and project).
6. Run the server and test the form.

Would you like to explore custom styling for the form or more advanced topics like ModelForms?