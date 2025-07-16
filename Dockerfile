# Use the official Python image from the Docker Hub, specifying the version
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY src/ ./src/

# Expose the port that the Flask app runs on
EXPOSE 5000

# Define the command to start the Flask application
CMD ["python", "src/app.py"]
