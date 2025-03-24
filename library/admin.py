from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Admin, Book, Student

admin.site.register(Admin)
admin.site.register(Book)
admin.site.register(Student)
