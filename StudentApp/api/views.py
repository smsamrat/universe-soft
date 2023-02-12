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
    def get(self, request, format=None):
        user = User.objects.all()
        # student = Student.objects.all()
        # course = Course.objects.all()
        one = UserRegistrationSerializer(user, many=True,context={'request': request})
        # two = StudentSerializers(student, many=True,context={'request': request})
        # three = CourseSerializers(course, many=True,context={'request': request})
        # comb = one.data + two.data + three.data
        return Response(one.data, status=status.HTTP_201_CREATED)
  
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

   
class CourseSerializerView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class  = CourseSerializers
    
class StudentSerializersView(APIView):   
    def get(self, request, format=None):
        user = StudentSerializers.objects.all()
        one = ArtistSerializer(user, many=True,context={'request': request})
        return Response(one.data, status=status.HTTP_201_CREATED)
  


    
    



