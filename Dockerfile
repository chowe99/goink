# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y postgresql-client \
    libpq-dev gcc \
    iputils-ping dnsutils \
    && rm -rf /var/lib/apt/lists/*

# Install Gunicorn
RUN pip install gunicorn

# Copy only requirements to leverage Docker cache
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "goink.wsgi:application", "--bind", "0.0.0.0:8000"]

