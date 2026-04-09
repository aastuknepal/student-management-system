from django.db import models

# Create your models here.


class Course(models.Model):

    #course details
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20, unique=True, help_text="e.g., PHY-101, CS-202")


    #academic Details

    DEPARTMNT_CHOICES = [
        ('cs', 'Computer Science'),
        ('math', 'Mathematics'),
        ('physics', 'Physics'),
        ('bio', 'Biology'),
        
    ]

    SEMESTER_CHOICES = [
       ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
         ('5', 'Fifth'),
        ('6', 'Sixth'),
        ('7', 'Seventh'),
        ('9', 'Eighth'),
        
    ]


    department = models.CharField(max_length=100,choices=DEPARTMNT_CHOICES, blank=True, null=True)
    credits = models.PositiveIntegerField(default=3, help_text="Number of credit hours")
    semester = models.CharField(blank=True, null=True, choices=SEMESTER_CHOICES, )


    #Relationships
    #Using a string reference "teacher.Teacher" prevents circular import error which is caused by importing as 'from teacher.moddels import Teacher'

    teacher = models.ForeignKey(
        'teacher.Teacher',
        on_delete=models.SET_NULL, 
        null = True,
        blank=True,
        related_name='assigned_course'
    )

    # on_delete=models.SET_NULL: If a teacher leaves the institution and their record is deleted,
    # the course itself shouldn't be deleted. Instead, 
    # the teacher field on this course will simply become null (unassigned) so you can assign a new teacher later.


    # related_name='assigned_courses': This is a powerful DRF/Django feature. 
    # It means if you have a Teacher object, you can easily find all courses they teach by querying teacher_instance.assigned_courses.all().

    created_at = models.DateTimeField(auto_now_add=True)

    #S
    is_deleted=models.BooleanField(default=False)



    def __str__(self):
        return f"{self.course_code} - {self.title}"