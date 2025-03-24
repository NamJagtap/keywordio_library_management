# library_management/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),  # Include the library app's URLs
]
# library_management/urls.py
from django.contrib import admin
from django.urls import path, include
from library.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add the home view to the root URL
    path('api/', include('library.urls')),  # Include the library app's URLs for the API
]
