from rest_framework import serializers

from StudentApp.models import UnivStudent

from django.contrib.auth import get_user_model
User = get_user_model()





class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('first_name','last_name','phone','email', 'password',)


class StudentSerializer(serializers.ModelSerializer):
    """
    A student serializer to return the student details
    """
    user = UserSerializer(required=True)
    class Meta:
        model = UnivStudent
        fields = ('user', 'subject_major',)
        read_only_fields = ('user',)
        

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = UnivStudent.objects.update_or_create(user=user,
                            subject_major=validated_data.pop('subject_major'))
        return student









# class UserRegistrationSerializer(serializers.ModelSerializer):
#   # We are writing this becoz we need confirm password field in our Registratin Request

#   password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
#   class Meta:
#     model = User
#     fields = ('first_name','last_name','phone','email', 'password',)
#     extra_kwargs={
#       'password':{'write_only':True}
#     }



# class StudentSerializer(serializers.ModelSerializer):
#   user = UserRegistrationSerializer(required=True)
#   class Meta:
#     model = Student
#     fields = ('user','net_fee','blood_group')
#     # read_only_fields = ['student']
    

#   def create(self, validated_data):
#       """
#       Overriding the default create method of the Model serializer.
#       :param validated_data: data containing all the details of student
#       :return: returns a successfully created student record
#       """
#       user_data = validated_data.pop('user')
#       user = UserRegistrationSerializer.create(UserRegistrationSerializer(), validated_data=user_data)
#       print(user)
#       students, created = Student.objects.update_or_create(subject_major=validated_data.pop('subject_major'))
#       return students
  


    


    

    
    
