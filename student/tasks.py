# File: student/tasks.py

import os
from celery import shared_task
from PIL import Image

@shared_task
def compress_image_task(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        return f"File {file_path} does not exist"

    try:
        # Open the image using Pillow
        img = Image.open(file_path)
        
        # Convert to RGB if the image has an alpha channel (like PNG)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        # Compress the image by overwriting it with a lower quality version
        img.save(file_path, optimize=True, quality=60)
        
        return f"Successfully compressed image at {file_path}"
    except Exception as e:
        return f"Failed to compress image: {str(e)}"
