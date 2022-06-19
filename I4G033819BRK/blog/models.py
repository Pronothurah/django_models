from email.headerregistry import Address
from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=23)
    Text = models.TextField(max_length=23)
    created_date = models.DateTimeField
    published_date = models.DateTimeField

class Country(models.Model):
    name = models.CharField(max_length=23)

