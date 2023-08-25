# We'll use an official Python image. You can also specify a version, e.g., python:3.9-slim
FROM python:3.9-slim

# Set the working directory in the Docker image
WORKDIR /app

# Copy the requirements.txt file into the image
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the image
COPY . .

# Specify the command to run when the image is started
CMD ["python", "runner.py"]
