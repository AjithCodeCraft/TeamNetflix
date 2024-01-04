from django.contrib import admin
from django.urls import path, include
  # Make sure the import statement is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ottApp.urls')),
      # Ensure the 'name' parameter is correct
]
