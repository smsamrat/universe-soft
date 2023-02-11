from rest_framework import serializers

from StudentApp.models import *
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.contrib.auth import get_user_model
from UserApp.models import User


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
       
class UserRegistrationSerializer(serializers.ModelSerializer):
    
    student_profile = StudentSerializers(required=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['first_name','last_name','phone','email', 'password', 'password2','student_profile']
        extra_kwargs={
        'password':{'write_only':True}
        }


    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validate_data):
        user_student = validate_data.pop('student_profile')
        user = User.objects.create(
            first_name = validate_data['first_name'],
            last_name = validate_data['last_name'],
            phone = validate_data['phone'],
            email = validate_data['email'],
            password = validate_data['password'],
        )
        Student.objects.update_or_create(
            student=user,
            net_fee = user_student['net_fee']
        )
        return user
    
    






    


    

    
    
