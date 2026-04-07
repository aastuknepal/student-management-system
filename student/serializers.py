from rest_framework import serializers
from .models import Student



from course.serializers import CourseSummarySerializer



#This will serialize the Student Class from Models.py

class StudentSerializer(serializers.ModelSerializer):

    course = CourseSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

    
