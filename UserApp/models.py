from django.db import models

from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name, phone, email, password=None, password2=None):
        """
        Creates and saves a User with the given first_name,last_name, phone, email, and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
        email=self.normalize_email(email),
        first_name =first_name,
        last_name =last_name,
        phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return 

    def create_superuser(self,first_name, last_name, phone, email, password=None):
        """
        Creates and saves a superuser with the given first_name,last_name, phone, email, and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
        )
        
        user.is_teacher = True
        user.is_student = True
        user.is_superadmin = True
        user.is_staff = True
        user.is_accountant = True
        user.save(using=self._db)
        return user

#  Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.EmailField(max_length=50, unique=True)
    phone =  models.CharField(max_length=50)
    
    #requird
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)# here is_active should be to for normal user to access home page after login
    is_superadmin = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name', 'phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
