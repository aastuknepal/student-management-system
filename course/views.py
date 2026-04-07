from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets

# Create your views here.

class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
