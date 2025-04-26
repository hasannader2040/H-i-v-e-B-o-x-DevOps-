# Stage 1: Versioning stage
FROM python:3.11-slim as version-stage

# Set the working directory
WORKDIR /app

# Copy only requirements.txt first to leverage Docker's cache
COPY requirements.txt /app/

# Install dependencies
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the files (including app_version.py)
COPY . /app

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the Python script for versioning
CMD ["python", "app_version.py"]

# ----------------------------------------




# Stage 2: Build and run stage for the Flask application
FROM python:3.11-slim as flask-stage

# Set the working directory
WORKDIR /app

# Copy everything from the version stage
COPY --from=version-stage /app /app

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]

# ----------------------------------------




# Stage 3: Testing the Flask application
FROM python:3.11-slim as test-stage

# Set the working directory
WORKDIR /app

# Copy everything from the Flask stage
COPY --from=flask-stage /app /app

# Install test dependencies (if separate)
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Test-specific CMD, can run tests if needed
CMD ["pytest", "test/integration"]




# (testing) tara@DESKTOP-VFLLPIU:/tmp/H-i-v-e-B-o-x-DevOps-/phase3$ ls
# Dockerfile  __init__.py  __pycache__  app.py  requirements.txt  test  tests
# (testing) tara@DESKTOP-VFLLPIU:/tmp/H-i-v-e-B-o-x-DevOps-/phase3$ cat Dockerfile


# # Stage 1: Versioning stage
# FROM python:3.11-slim as version-stage
#
# # Set the working directory
# WORKDIR /app
#
# # Copy only requirements.txt first to leverage Docker's cache
# COPY phase3/requirements.txt /app/
#
# # Install dependencies
# RUN pip3 install --no-cache-dir -r /app/requirements.txt
#
# # Copy the rest of the files (including app_version.py)
# COPY . /app
#
# # Define environment variable
# ENV PYTHONUNBUFFERED=1
#
# # Run the Python script for versioning
# CMD ["python", "app_version.py"]
#
# # ----------------------------------------
#
# # Stage 2: Build and run stage for the Flask application
# FROM python:3.11-slim as flask-stage
#
# # Set the working directory
# WORKDIR /app
#
# # Copy everything from the version stage
# COPY --from=version-stage /app /app
#
# # Expose port 5000
# EXPOSE 5000
#
# # Run the Flask application
# CMD ["flask", "run", "--host=0.0.0.0"]
#
# # ----------------------------------------
#
# # Stage 3: Testing the Flask application
# FROM python:3.11-slim as test-stage
#
# # Set the working directory
# WORKDIR /app
#
# # Copy everything from the Flask stage
# COPY --from=flask-stage /app /app
#
# # Install test dependencies (if separate)
# COPY phase3/requirements.txt /app/
# RUN pip3 install --no-cache-dir -r /app/requirements.txt
#
# # Test-specific CMD, can run tests if needed
# CMD ["pytest", "test/integration"]