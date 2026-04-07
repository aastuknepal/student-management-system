from .models import Course
from rest_framework import serializers


from teacher.serializers import TeacherSummarySerializer


#serialize all course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'





#This is to show nested json in student to show course detail in the student detail's json
        
class CourseSummarySerializer(serializers.ModelSerializer):

    teacher = TeacherSummarySerializer(read_only=True)
    class Meta:
        model = Course
        # Only list the specific fields you want to show in the nested JSON!
        fields = ['title', 'department', 'teacher']