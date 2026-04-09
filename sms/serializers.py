from django.contrib.auth.models import User, Group
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})
    role = serializers.ChoiceField(choices=['Student', 'Teacher', 'Admin'], write_only=True, required=False)


    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role']


    def create(self, validated_data):
        
        role = validated_data.pop('role', 'Student')

        request = self.context.get('request')

        is_admin = request and request.user.is_authenticated and (
            request.user.is_superuser or request.user.groups.filter(name='Admin').exists()
        )

        if role in ['Admin', 'Teacher'] and not is_admin:
            raise serializers.ValidationError({"role": f"You dont have permission to create  {role} account."})
        
        #Create the user 
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email',),
            password=validated_data['password'],
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', '')
        )

#Assign the group
        try:
            group = Group.objects.get(name=role)
            user.groups.add(group)
        except Group.DoesNotExist:
            pass

        return user
        