# library/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, BookViewSet, StudentView

router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Register the viewsets with the router
    path('api/student/books/', StudentView.as_view(), name='student-books'),  # Student view to list all books
]
