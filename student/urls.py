from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewset

# Set up the router for the ViewSet
router = DefaultRouter()
router.register(r'students', StudentViewset, basename='student')

# Define the URL patterns for this app
urlpatterns = [

    # This automatically creates all the routes for  ViewSet (GET, POST, PUT, DELETE)
    path('', include(router.urls)),
    
]