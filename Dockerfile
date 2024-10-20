# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*


# Install dependencies first
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the rest of the code
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

