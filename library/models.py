from django.db import models

# Create your models here.
# library/models.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=20)
    page_count = models.IntegerField()

    def __str__(self):
        return self.title

# library/models.py
from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # We will hash this password

    def __str__(self):
        return self.email


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# library/models.py
from django.db import models

class Admin(models.Model):
    # Your fields for the Admin model
    pass

class Book(models.Model):
    # Your fields for the Book model
    pass

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # Add any other relevant fields for the student model
    books = models.ManyToManyField(Book)  # If students have many books

    def __str__(self):
        return self.name
