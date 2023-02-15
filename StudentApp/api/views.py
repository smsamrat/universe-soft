from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from UserApp.models import User
from StudentApp.api.serializers import *
from StudentApp.models import *
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import authenticate
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

    # User Registration Functionality #

class StudentRegistrationView(APIView):
    def get(self, request,id=None, format=None):
        id=id
        if id is not None:
            single_user = User.objects.get(id=id)
            serializer = StudentRegistrationSerializer(single_user)
            return Response(serializer.data)
        user = User.objects.filter(is_student=True)
        serializer = StudentRegistrationSerializer(user, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    def post(self, request, format=None):
        serializer = StudentRegistrationSerializer(data=request.data)
        # parser_classes = [parsers.FormParser, parsers.MultiPartParser]
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,format=None):
        id = id
        single_user = User.objects.get(id=id)
        data=request.data
        print(data)

        student_profile = Student.objects.get(student=single_user)
        student_profile.net_fee = data["student_profile"]["net_fee"]
        student_profile.course_id = data["student_profile"]["course"]
        student_profile.save()
        
        single_user.first_name = data["first_name"]
        single_user.save()

        serializer = StudentSerializers(student_profile)
        serializer = StudentRegistrationSerializer(single_user)
        return Response(serializer.data)
    
# Teacher Registration Functionality #

class TeacherRegistrationView(APIView):
    def get(self, request,id=None, format=None):
        id=id
        if id is not None:
            single_user = User.objects.get(id=id)
            serializer = TeacherRegistrationSerializer(single_user)
            return Response(serializer.data)
        user = User.objects.filter(is_teacher=True)
        serializer = TeacherRegistrationSerializer(user, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    def post(self, request, format=None):
        serializer = TeacherRegistrationSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.is_teacher = True
            instance.is_student = False
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,format=None):
        id = id
        single_user = User.objects.get(id=id)
        data=request.data
        print(data)

        teacher_profile = Teacher.objects.get(teacher=single_user)
        teacher_profile.name = data['teacher_profile']["name"]
        teacher_profile.address = data['teacher_profile']["address"]
        teacher_profile.designation = data['teacher_profile']["designation"]
        teacher_profile.education = data['teacher_profile']["education"]
        teacher_profile.image = data['teacher_profile']["image"]
        teacher_profile.blood_group = data['teacher_profile']["blood_group"]
        teacher_profile.gender = data['teacher_profile']["gender"]
        teacher_profile.occupation = data['teacher_profile']["occupation"]
        teacher_profile.save()

        single_user.first_name = data["first_name"]
        single_user.last_name = data["last_name"]
        single_user.phone = data["phone"]
        single_user.email = data["email"]
        single_user.save()

        serializer = TeacherSerializer(teacher_profile)
        serializer = TeacherRegistrationSerializer(single_user)
        return Response(serializer.data)
    


    # User Login Functionality #
    
class UserLogin(APIView):
    def post(self, request, format=None):
        serializer =  UserLoginSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            email =  serializer.data.get('email')
            print(email)
            password =  serializer.data.get('password')
            print(password)
            user = authenticate(email=email,password=password)
            print(user)
            if user is not None:
                return Response({ 'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
  

    # User Login Functionality #
    
class UserLogin(APIView):
    def post(self, request, format=None):
        serializer =  UserLoginSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            email =  serializer.data.get('email')
            print(email)
            password =  serializer.data.get('password')
            print(password)
            user = authenticate(email=email,password=password)
            print(user)
            if user is not None:
                return Response({ 'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        



   # Course CRUD  Functionality #  
   
class CourseSerializerView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class  = CourseSerializers
    
    
# StudentProfile CRUD  Functionality # 
   
class StudentProfileView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class  = StudentSerializers
    

  


    
    



