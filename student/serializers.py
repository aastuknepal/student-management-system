from rest_framework import serializers
from .models import Student



from course.serializers import CourseSummarySerializer
from teacher.serializers import TeacherSerializer



#This will serialize the Student Class from Models.py

class StudentSerializer(serializers.ModelSerializer):

    course_name = CourseSummarySerializer(source='course', many=True, read_only=True)
    teacher_detail = TeacherSerializer(source='teacher', read_only=True)

    class Meta:
        model = Student
        # fields = ['name', 'roll_number', 'email', 'date_of_birth', 'semester', 'phone_number', 'guardian_name', 'enrollment_date', 'course', 'course_name']
        fields = ['name', 'gender', 'roll_number', 'email', 'date_of_birth', 'semester', 'phone_number', 'guardian_name', 'enrollment_date', 'course', 'course_name', 'teacher_detail']


    
