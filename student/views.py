from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    #Soft deleting the records
    
    def destroy(self, request, *args, **kwargs):

        student = self.get_object()
        student.is_deleted = True
        student.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    def get_queryset(self):
        return Student.objects.filter(is_deleted=False)



    

