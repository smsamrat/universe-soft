from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from UserApp.models import User
from StudentApp.api.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser



# class StudentRecordView(APIView):
#     """
#     A class based view for creating and fetching student records
#     """
#     def get(self, format=None):
#         """
#         Get all the student records
#         :param format: Format of the student records to return to
#         :return: Returns a list of student records
#         """
#         students = UnivStudent.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         """
#         Create a student record
#         :param format: Format of the student records to return to
#         :param request: Request object for creating student
#         :return: Returns a student record
#         """
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages,
#                         status=status.HTTP_400_BAD_REQUEST)

# # class UserRegistrationView(APIView):
#     # queryset = User.objects.all()
#     # serializer_class = UserRegistrationSerializer

class UserRegistrationView(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        student = Student.objects.all()
        one = UserRegistrationSerializer(user, many=True,context={'request': request})
        two = StudentSerializers(student, many=True,context={'request': request})
        comb = one.data + two.data
        return Response(comb, status=status.HTTP_201_CREATED)
  
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
