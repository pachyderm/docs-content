# syntax=docker/dockerfile:1 

FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the rest of the application code into the container
COPY . .

# Run the command to start the pipeline
CMD ["python", "count.py"]
