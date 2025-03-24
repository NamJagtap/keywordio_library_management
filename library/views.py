# library/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Admin, Book, Student
from .serializers import AdminSerializer, BookSerializer, StudentSerializer

# Admin ViewSet
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

# Book ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Student View to list all books
class StudentView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Library Management System!")
