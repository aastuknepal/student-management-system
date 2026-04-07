from django.shortcuts import render
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework import viewsets

# Create your views here.

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer