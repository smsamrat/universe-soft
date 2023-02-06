from UserApp.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from UserApp.api.serializers import UserCreationSerializer
from rest_framework.generics import ListCreateAPIView,CreateAPIView,ListAPIView




class UserRegistrationView(ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    
    
    # def post(self, request, format=None):
    #     serializer = UserCreationSerializer(data = request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         user = serializer.save()
    #     return Response({'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    
            
        
    