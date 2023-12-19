# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the Python source code into the container
COPY . .

# Command to run the FastAPI application using Uvicorn
CMD [ "python", "Monitoring-gRPC/server.py"]