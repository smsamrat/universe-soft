from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=120)
    duration = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name
     
class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    batch_number = models.IntegerField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batches"
        ordering = ["-id"]
    
    def __str__(self):
        return f'{self.course} ({self.batch_number})'
     
class Student(models.Model):
    name = models.CharField(max_length=120)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=120)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=120)
    transaction_id = models.CharField(max_length=120)
    course_fee = models.IntegerField()
    discount = models.IntegerField()
    net_fee = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.IntegerField()
    reference_by = models.CharField(max_length=120)
    password1 = models.CharField(max_length=120)
    created_at = models.DateTimeField(max_length=120)
    updated_at = models.DateTimeField(max_length=120)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name



class StudentProfile(models.Model):
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    image = models.ImageField(upload_to="student")
    blood_group = models.CharField(max_length=255, choices=BLOOD_GROUP_CHOICE)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICE)
    occupation = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "StudentProfile"
        verbose_name_plural = "StudentProfile"
        ordering = ["-id"]
    

    def __str__(self):
        return self.student.name


class Teacher(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    designation = models.CharField(max_length=120)
    education = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to="teacher")
    created_at = models.DateTimeField(max_length=120)
    updated_at = models.DateTimeField(max_length=120)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name


class CollectionType(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "CollectionType"
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
    created_at = models.DateTimeField(max_length=120)
    updated_at = models.DateTimeField(max_length=120)

    class Meta:
        verbose_name = "AdditionalCollection"
        verbose_name_plural = "AdditionalCollections"
        ordering = ["-id"]
    
    def __str__(self):
        return self.provider



class ExpenseType(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ExpenseType"
        verbose_name_plural = "ExpenseTypes"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=120)
    id_number = models.IntergerField()
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    amount = models.IntegerField()
    phone_number = PhoneNumberField()
    email = models.EmailField()
    status = models.DateField()
    created_at = models.DateTimeField(max_length=120)
    updated_at = models.DateTimeField(max_length=120)

    class Meta:
        verbose_name = "AdditionalCollection"
        verbose_name_plural = "AdditionalCollections"
        ordering = ["-id"]
    
    def __str__(self):
        return self.provider



     