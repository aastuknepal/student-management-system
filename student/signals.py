# File: student/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from .tasks import compress_image_task

@receiver(post_save, sender=Student)
def compress_student_photo(sender, instance, created, **kwargs):
    # Trigger task if photo exists
    if instance.photo:
        file_path = instance.photo.path
        
        # Send the task to Celery to be executed in the background
        compress_image_task.delay(file_path)
