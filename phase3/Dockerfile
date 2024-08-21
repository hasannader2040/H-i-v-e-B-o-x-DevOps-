# Stage 1: Build stage for the app_version.py
FROM python:3.11-slim as version-stage

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run the Python script when the container launches
CMD ["python", "app_version.py"]




# ////////////////////////////////////////////////////

# Stage 2: Build and run stage for the Flask application
FROM python:3.8-slim-buster as flask-stage

# Copy requirements.txt for dependency installation
COPY requirements.txt /app/requirements.txt

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 5000
EXPOSE 5000

# Run the Flask application
 CMD ["flask", "run", "--host=0.0.0.0"]  
 # to expose to outside of the cointiner  "--host=0.0.0.0"


#  stage 3. 



