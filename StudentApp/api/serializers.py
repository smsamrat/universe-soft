from rest_framework import serializers

from StudentApp.models import *
from django.conf import settings
from django.contrib.auth import get_user_model
from UserApp.models import User


# Add student section area
  
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student','course','net_fee','image','blood_group']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['course'] = {"name":instance.course.name,"duration":instance.course.duration}
        return data

class CourseSerializers(serializers.ModelSerializer):
    courseby = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ['name','duration','courseby']
       
class StudentRegistrationSerializer(serializers.ModelSerializer):
    
    student_profile = StudentSerializers(required=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['first_name','last_name','phone','email', 'password', 'password2','student_profile',
                'is_student'
                ]
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
        try:
            for uploaded_item in user_student:
                Student.objects.update_or_create(
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
    
# Add teacher section area
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
    
class TeacherRegistrationSerializer(serializers.ModelSerializer):
    teacher_profile = TeacherSerializer(required=True)
    
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['first_name','last_name','phone','email', 'password', 'password2', 'teacher_profile']
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
        user_teacher = validate_data.pop('teacher_profile')
        user = User.objects.create(
            first_name = validate_data['first_name'],
            last_name = validate_data['last_name'],
            phone = validate_data['phone'],
            email = validate_data['email'],
            password = validate_data['password'],
        )
        try:
            Teacher.objects.update_or_create(
            teacher=user,
            name = user_teacher['name'],
            address = user_teacher['address'],
            designation = user_teacher['designation'],
            education = user_teacher['education'],
            image = user_teacher['image'],
            blood_group = user_teacher['blood_group'],
            gender = user_teacher['gender'],
            occupation = user_teacher['occupation'],

                
        )
        except:
            Teacher.objects.update_or_create(
            teacher=user,
            name = user_teacher['name'],
            address = user_teacher['address'],
            designation = user_teacher['designation'],
            education = user_teacher['education'],
            # image = user_teacher['image'],
            blood_group = user_teacher['blood_group'],
            gender = user_teacher['gender'],
            occupation = user_teacher['occupation'],
        )
            
        return user  

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']
        

    







    


    

    
    
