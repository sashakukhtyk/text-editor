# Use an official Python runtime as a parent image
FROM python:3.12.2

# Install dependencies for PyQt5 and OpenGL
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libxext6 \
    libxrender1 \
    libxcb1 \
    libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy your application files into the container
COPY main.py .
COPY editor.ui .

# Set the environment variable to use the container's display
ENV DISPLAY=:0

# Command to run your application
CMD ["python", "main.py"]
