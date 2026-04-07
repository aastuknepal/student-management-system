from django.db import models

# Create your models here.


class Teacher(models.Model):


    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100, null=True)
    date_of_joining = models.DateField()

    description = models.TextField(blank=True, null=True)



    def __str__(self):
        return f"{self.name}"
