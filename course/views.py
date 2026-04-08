from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.

class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


    def destroy(self, request, *args, **kwargs):

        course = self.get_object()

        #This soft deletes the record i.e it just hides the deleted data from the database instead of deleting, this changes the flag to true which 
        #is later used to filter out the records while get request is made
        course.is_deleted=True
        course.save()

        #Send back standard 204(no content) success response
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #This hides the deleted course from the get request and onlt show the records that has the flag set to false by default
    
    def get_queryset(self):
        return Course.objects.filter(is_deleted=False)
