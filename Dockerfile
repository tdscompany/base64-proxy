# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the Docker image
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run app.py when the container launches using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app"]
