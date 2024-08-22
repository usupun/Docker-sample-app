# Base image
FROM python:3.11.0

# Set the working directory
WORKDIR /app

# Copy the application files
COPY main-app/app.py .

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the application
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]