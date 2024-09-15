# Use an official Python runtime as a parent image
FROM python:3.12.2

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy your application files into the container
COPY main.py .
COPY editor.ui .

# Set the environment variable to use the container's display
ENV DISPLAY=:0

# Command to run your application
CMD ["python", "main.py"]