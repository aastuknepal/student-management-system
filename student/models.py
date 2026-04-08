from django.db import models

# Create your models here.

class Student(models.Model):

    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    gender = models.CharField(max_length=10, choices= GENDER_CHOICES, blank=True, null=True)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    semester = models.PositiveIntegerField(blank=True, null=True, help_text="Semester :1, 2, 3...")



    phone_number = models.CharField(max_length=15, blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)


    enrollment_date = models.DateField(auto_now_add=True)
    course = models.ManyToManyField('course.Course', related_name='student', blank=True)  

    is_deleted=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} ({self.roll_number})"
