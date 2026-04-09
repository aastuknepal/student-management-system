from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer, StudentRestrictedSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

# This is only to lock user from viewing the student page its commented because global lock is applied which requires to login to view any student or teacher or course
# from rest_framework.permissions import IsAuthenticated
# from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from sms.permissions import StudentAccessPermission


# Create your views here.


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [StudentAccessPermission]

    # This method dynamically choses which serializer to use 
    def get_serializer_class(self):
        user = self.request.user

        # If the user is an Admin or Teacher, give them full data
        if user.groups.filter(name__in=['Admin', 'Teacher']).exists() or user.is_superuser:
            return StudentSerializer
        
        # Otherwise if they are just student give them the restricted serializer which has limited data
        return StudentRestrictedSerializer
         

    #This locks the endpoint down, it is applied only to this view when not made comment, 
    # permission_classes = [IsAuthenticated]


    #Soft deleting the records
    
    def destroy(self, request, *args, **kwargs):

        student = self.get_object()
        student.is_deleted = True
        student.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    def get_queryset(self):
        return Student.objects.filter(is_deleted=False)

'''

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
'''

