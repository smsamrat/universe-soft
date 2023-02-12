from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
##################################################################################
"""Course Section"""
##################################################################################


class Course(models.Model):
    name = models.CharField(max_length=120)
    duration = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Courses"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name+" "+self.duration


##################################################################################
"""Teacher Section"""
##################################################################################

class Teacher(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom')
    )
    BLOOD_GROUP_CHOICE = (
        ('A+', 'A(+ve)'),
        ('A-', 'A(-ve)'),
        ('B+', 'B(+ve)'),
        ('B-', 'B(-ve)'),
        ('O+', 'O(+ve)'),
        ('O-', 'O(-ve)'),
        ('AB+', 'AB(+ve)'),
        ('AB-', 'AB(-ve)')
    )
    teacher = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="teacher_profile")
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)
    education = models.CharField(max_length=255)
    image = models.ImageField(upload_to="teacher")
    blood_group = models.CharField(max_length=255, choices=BLOOD_GROUP_CHOICE)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICE)
    occupation = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Teacher"
        ordering = ["-id"]
    

    def __str__(self):
        return self.name



##################################################################################
"""Batch Section"""
##################################################################################



class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    batch_number = models.IntegerField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Batches"
        ordering = ["-id"]
    
    def __str__(self):
        return f'{self.course} ({self.batch_number})'


class ClassRoutine(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    day = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ClassRoutines"
        ordering = ["-id"]
    
    def __str__(self):
        return f'{self.batch.course.name} ({self.batch.batch_number})'


##################################################################################
"""Student Section"""
##################################################################################
   
class Student(models.Model):
    # PAYMENT_CHOICE = (
    #     ('Cash', 'Cash'),
    #     ('Bkash', 'Bkash'),
    #     ('Nagad', 'Nagad'),
    #     ('Rocket', 'Rocket')
    # )
    # GENDER_CHOICE = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('C', 'Custom')
    # )
    BLOOD_GROUP_CHOICE = (
        ('A+', 'A(+ve)'),
        ('A-', 'A(-ve)'),
        ('B+', 'B(+ve)'),
        ('B-', 'B(-ve)'),
        ('O+', 'O(+ve)'),
        ('O-', 'O(-ve)'),
        ('AB+', 'AB(+ve)'),
        ('AB-', 'AB(-ve)')
    )
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile",null=True,blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True,related_name="courseby")
    # course_type = models.CharField(max_length=120)
    # batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    # payment_method = models.CharField(max_length=50,choices=PAYMENT_CHOICE)
    # transaction_id = models.CharField(max_length=120)
    # course_fee = models.IntegerField()
    # discount = models.IntegerField()
    net_fee = models.IntegerField()
    # paid_amount = models.IntegerField()
    # due_amount = models.IntegerField()
    # reference_by = models.CharField(max_length=120)
    # address = models.CharField(max_length=120)
    image = models.ImageField(upload_to="student", blank=True, null=True)
    blood_group = models.CharField(max_length=255,blank=True, null=True, choices=BLOOD_GROUP_CHOICE)
    # gender = models.CharField(max_length=255, choices=GENDER_CHOICE)
    # occupation = models.CharField(max_length=120)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Students"
        ordering = ["-id"]
    
    





# class StudentProfile(models.Model):
#     GENDER_CHOICE = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('C', 'Custom')
#     )
#     BLOOD_GROUP_CHOICE = (
#         ('A+', 'A(+ve)'),
#         ('A-', 'A(-ve)'),
#         ('B+', 'B(+ve)'),
#         ('B-', 'B(-ve)'),
#         ('O+', 'O(+ve)'),
#         ('O-', 'O(-ve)'),
#         ('AB+', 'AB(+ve)'),
#         ('AB-', 'AB(-ve)')
#     )
#     # student = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
#     address = models.CharField(max_length=120)
#     image = models.ImageField(upload_to="student", blank=True, null=True)
#     blood_group = models.CharField(max_length=255, choices=BLOOD_GROUP_CHOICE)
#     gender = models.CharField(max_length=255, choices=GENDER_CHOICE)
#     occupation = models.CharField(max_length=120)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)


#     class Meta:
#         verbose_name_plural = "StudentProfile"
#         ordering = ["-id"]
    

#     def __str__(self):
#         return self.student.name


##################################################################################
"""Additional Collection Section"""
##################################################################################


class CollectionType(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "CollectionTypes"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name


class AdditionalCollection(models.Model):
    provider = models.CharField(max_length=120)
    receiver = models.CharField(max_length=120)
    collection_type = models.ForeignKey(CollectionType, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=120)
    transaction_id = models.CharField(max_length=120)
    amount = models.IntegerField()
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "AdditionalCollections"
        ordering = ["-id"]
    
    def __str__(self):
        return self.provider


##################################################################################
"""Expense Section"""
##################################################################################



class ExpenseType(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ExpenseTypes"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=120)
    id_number = models.IntegerField()
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    amount = models.IntegerField()
    phone_number = PhoneNumberField()
    email = models.EmailField()
    status = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "AdditionalCollections"
        ordering = ["-id"]
    
    def __str__(self):
        return self.provider



##################################################################################
"""Load and Deposit Section"""
##################################################################################

class AccountType(models.Model):
    name = models.CharField(max_length=120)
    max_amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "AccountType"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name


class BankAccount(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom')
    )
    user = models.CharField(max_length=120)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    account_number = models.IntegerField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICE)
    date_of_birth = models.DateField()
    balance = models.IntegerField()
    deposit_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "BankAccounts"
        ordering = ["-id"]
    
    def __str__(self):
        return self.user

class UserAddress(models.Model):
    user = models.ForeignKey(BankAccount, related_name='user_address', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.DateField()
    country = CountryField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "UserAddress"
        ordering = ["-id"]
    
    def __str__(self):
        return self.user


class TransactionType(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "TransactionType"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    amount = models.IntegerField()
    remaining_money = models.IntegerField()
    deposit_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Transactions"
        ordering = ["-id"]
    
    def __str__(self):
        return self.user

     