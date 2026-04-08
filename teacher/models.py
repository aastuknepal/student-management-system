from django.db import models

# Create your models here.


class Teacher(models.Model):


    DEPARTMNT_CHOICES = [
        ('cs', 'Computer Science'),
        ('math', 'Mathematics'),
        ('physics', 'Physics'),
        ('bio', 'Biology'),
        ('Mlt', 'Multiple')
    ]


    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100,choices=   DEPARTMNT_CHOICES, default='Mlt')
    date_of_joining = models.DateField()

    description = models.TextField(blank=True, null=True)

    is_deleted=models.BooleanField(default=False)




    def __str__(self):
        return f"{self.name}"
