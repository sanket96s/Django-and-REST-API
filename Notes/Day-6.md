**Day 6: Django Templates — Using Templates to Render HTML**

Django templates are used to render dynamic HTML content. They allow you to separate the presentation (HTML) from the business logic (Python code). This approach makes it easier to maintain and scale your applications. Let’s break down the key subtopics related to using templates in Django.

### 1. **What is a Django Template?**
A **Django template** is essentially a text file that can generate HTML dynamically. It contains both the static HTML code and dynamic content that will be rendered by the server. The dynamic content is inserted through Django's templating language, which uses **placeholders** for variables and **tags** to control the flow of the HTML output.

### 2. **Setting Up Django Templates**
Django comes with a built-in template system. To use templates in a Django project, follow these steps:

- **Template Directory**: In your Django project settings (`settings.py`), define the template directory:
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

- **App-specific Templates**: You can also create a `templates` folder within each app to store templates.

### 3. **Rendering Templates in Views**
To render a template in a view, use the `render()` function provided by Django. It takes the request, template name, and context data (variables) as parameters.

Example:
```python
from django.shortcuts import render

def my_view(request):
    context = {'name': 'John', 'age': 25}
    return render(request, 'my_template.html', context)
```
In this example, `my_template.html` is rendered, and the variables `name` and `age` are passed to the template.

### 4. **Template Syntax — Variables**
Django templates allow you to insert dynamic content using variables enclosed in `{{ }}`. You can use these variables to display data from the context passed from the view.

Example:
```html
<p>Hello, {{ name }}! You are {{ age }} years old.</p>
```
If the context is `{'name': 'John', 'age': 25}`, the output will be:
```html
<p>Hello, John! You are 25 years old.</p>
```

### 5. **Template Tags**
Django provides **tags** enclosed in `{% %}` to handle logic like loops, conditionals, and blocks. Tags are used to control the flow or manipulate data.

#### Common Template Tags:
- **Conditionals**:
  ```html
  {% if user.is_authenticated %}
      <p>Welcome, {{ user.username }}!</p>
  {% else %}
      <p>Welcome, guest!</p>
  {% endif %}
  ```

- **For Loops**:
  ```html
  <ul>
  {% for item in items %}
      <li>{{ item }}</li>
  {% endfor %}
  </ul>
  ```

- **Template Filters**: Filters are used to modify variables in templates.
  Example:
  ```html
  {{ name|lower }}  <!-- Converts name to lowercase -->
  ```

- **Include**: You can include other templates within a template.
  ```html
  {% include 'header.html' %}
  ```

### 6. **Template Inheritance**
Django templates allow for inheritance, meaning you can define a **base template** that other templates can extend. This helps avoid redundancy and makes maintenance easier.

- **Base Template** (`base.html`):
  ```html
  <!DOCTYPE html>
  <html>
      <head>
          <title>{% block title %}My Site{% endblock %}</title>
      </head>
      <body>
          <header>
              <h1>My Site</h1>
          </header>
          <div>
              {% block content %}{% endblock %}
          </div>
      </body>
  </html>
  ```

- **Child Template** (`home.html`):
  ```html
  {% extends 'base.html' %}
  {% block content %}
      <p>Welcome to the homepage!</p>
  {% endblock %}
  ```

In this example, `home.html` extends `base.html`, and the content in the `{% block content %}` section is replaced by the content in the child template.

### 7. **Static Files in Templates**
Static files like CSS, JavaScript, and images are usually stored in the `static` directory. You can use the `{% static %}` tag to link static files in your templates.

Example:
```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}">
```

### 8. **Template Context**
The **context** is a dictionary passed from the view to the template. It contains data that will be inserted into the template variables.

Example:
```python
def my_view(request):
    context = {'name': 'Alice', 'message': 'Hello World'}
    return render(request, 'my_template.html', context)
```
In the template, you can use:
```html
<p>{{ name }} says: {{ message }}</p>
```

### 9. **Template Debugging**
To debug templates in Django, you can use:
- **`{% debug %}`**: This will print all available context variables.
- **Django Template Errors**: Django provides detailed error messages with line numbers if a template rendering fails.

Example:
```html
{% debug %}
```

### 10. **Best Practices**
- Use **template inheritance** to avoid code duplication.
- Keep logic out of templates. Templates should only be responsible for presentation.
- Use **static files** for styles and scripts rather than embedding them directly into HTML.
- Always use **escaping** in templates to prevent security risks like XSS (Cross-Site Scripting).

### 11. **Advanced Template Features**
- **Custom Template Filters**: You can define custom filters in `templatetags` to extend Django’s templating system.
- **Template Subclassing**: In Django 3.0+, you can use template subclassing for more advanced templating strategies.

By using Django templates effectively, you can keep your web application's presentation layer clean and maintainable while easily integrating dynamic content.