from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'




class TeacherSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'department']