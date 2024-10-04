# Stage 1: Build stage for app_version.py
FROM python:3.12-slim-bookworm as version-stage

# Set the working directory
WORKDIR /app

# Copy only requirements.txt first to leverage Docker's cache
COPY requirements.txt /app/

# Install dependencies
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the files (including app_version.py)
COPY . /app

# Define environment variable
ENV PYTHONUNBUFFERED 1


# Run the Python script for versioning
CMD ["python", "app_version.py"]


# ----------------------------------------


# Stage 2: Build and run stage for the Flask application
FROM python:3.12-slim-bookworm as flask-stage

# Set the working directory
WORKDIR /app

# Copy requirements.txt for dependency installation // I am confused with the requirements of evey stage 
COPY --from=version-stage /app /app

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