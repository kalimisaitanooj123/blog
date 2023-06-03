from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Blog(models.Model):
    name=models.CharField(max_length=255)
    title=models.CharField(max_length=255,unique=True)
    content=models.TextField(max_length=10000000)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # feature_image = models.ImageField(upload_to="uploads/", null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    comments = models.CharField(max_length=100)
    phone=models.IntegerField(null=True)

    def __str__(self):
        return self.name