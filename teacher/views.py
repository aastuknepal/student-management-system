from django.shortcuts import render
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


# Create your views here.

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



    #This turn on the filter and search backends

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    #This search for partial match

    search_fields = ['name', 'description', 'department']

    # # 2. Define EXACT match fields (django-filter)
    # filterset_fields = ['department', 'date_of_joining']


    #Soft deleting of the records

    def destroy(self, request, *args, **kwargs):
        teacher = self.get_object()
        teacher.is_deleted =True
        teacher.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_queryset(self):
        return Teacher.objects.filter(is_deleted=False)