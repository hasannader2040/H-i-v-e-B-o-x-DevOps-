# Stage 1: Build stage for app_version.py
FROM python:3.11-slim as version-stage

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run the Python script for versioning
CMD ["python", "app_version.py"]


# ----------------------------------------


# Stage 2: Build and run stage for the Flask application
FROM python:3.11-slim as flask-stage

# Set the working directory
WORKDIR /app

# Copy requirements.txt for dependency installation // I am confused with the requirements of evey stage 
COPY --from=version-stage /app /app

# Install dependencies
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . /app

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]


# ----------------------------------------


# Stage 3: Testing the Flask application 
FROM python:3.11-slim as test-stage

COPY --from=flask-stage /app /app


# Test-specific CMD, can run tests if needed
CMD ["pytest", "tests/"]


