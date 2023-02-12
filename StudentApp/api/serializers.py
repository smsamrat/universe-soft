from rest_framework import serializers

from StudentApp.models import *
from django.conf import settings
from django.contrib.auth import get_user_model
from UserApp.models import User


  
class StudentSerializers(serializers.ModelSerializer):
    course = HyperlinkedIdentityField(view_name='course-detail')
    class Meta:
        model = Student
        fields = ['student','course','net_fee','image','blood_group']



class CourseSerializers(serializers.ModelSerializer):
    courseby = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ['name','duration','courseby']
       
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
        print(user_student)
        user = User.objects.create(
            first_name = validate_data['first_name'],
            last_name = validate_data['last_name'],
            phone = validate_data['phone'],
            email = validate_data['email'],
            password = validate_data['password'],
        )
        try:
            for uploaded_item in user_student:
                print(uploaded_item)
                Student.objects.create(
                student=user,
                course = user_student['course'],
                net_fee = user_student['net_fee'],
                image = uploaded_item,
                blood_group = user_student['blood_group'],
                )
        except:
            Student.objects.update_or_create(
                student=user,
                course = user_student['course'],
                net_fee = user_student['net_fee'],
                blood_group = user_student['blood_group'],
            )
        return user
    
    







    


    

    
    
