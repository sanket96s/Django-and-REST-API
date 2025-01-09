from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_created=True)
    
    