from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User



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

class StudentRestrictedSerializer(serializers.ModelSerializer):
    course_details = CourseSummarySerializer(source='course', many=True, read_only=True)

    class Meta:
        model = Student
        # Student will be able to view only these fields
        
        fields = ['id', 'name','gender', 'semester','course_details']


#Since the registration is global feature and moved to the sms main app its commented out
'''
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User

        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data.get('email', ''),
            first_name = validated_data.get('first_name',''),
            last_name = validated_data.get('last_name','')
        )

        return user


'''