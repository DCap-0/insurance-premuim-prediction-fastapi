# base image
FROM python:3.11-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# # In case requirements leads to some issues
# COPY requirements-lock.txt .
# RUN pip install --no-cache-dir -r requirements-lock.txt

# Copy the rest of application code
COPY . .

# Expose application port
EXPOSE 8000

# Command to start FastAPI application
CMD [ "uvicorn", "app:main:app", "--host", "0.0.0.0", "--port", "8000" ]