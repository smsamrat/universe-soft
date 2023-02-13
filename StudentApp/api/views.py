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

class UserRegistrationView(APIView):
    def get(self, request,id=None, format=None):
        id=id
        if id is not None:
            single_user = User.objects.get(id=id)
            serializer = UserRegistrationSerializer(single_user)
            return Response(serializer.data)
        user = User.objects.all()
        serializer = UserRegistrationSerializer(user, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,format=None):
        id = id
        single_user = User.objects.get(pk=id)
        data=request.data
        print(data)

        student_profile = Student.objects.get(student=single_user)
        student_profile.net_fee = data["student_profile"]["net_fee"]
        student_profile.course_id = data["student_profile"]["course"]
        student_profile.save()
        
        single_user.first_name = data["first_name"]
        single_user.save()

        serializers = StudentSerializers(student_profile)
        serializers = UserRegistrationSerializer(single_user)
        return Response(serializers.data)
    
# class UserRegistrationDetailView(APIView):
#     def get(self, request,pk, format=None):
#         user = User.objects.get(pk=pk)
#         one = UserRegistrationSerializer(user)
#         return Response(one.data, status=status.HTTP_201_CREATED)
    
#     def put(self, request, pk, format=None):
#         single_user = self.get_object(pk=pk)
#         serializer = SnippetSerializer(single_user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
   
class CourseSerializerView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class  = CourseSerializers
    
class StudentProfileView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class  = StudentSerializers
  


    
    



