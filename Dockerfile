# Use python rintime as parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (helps with Pillow and other builds)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirement.txt /app/
RUN pip install --no-cache-dir -r requirement.txt

# Copy the project code into the container
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Default command to run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]