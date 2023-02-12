# Python version
FROM python:3.11

# Set a working directory inside docker vm
WORKDIR /fastapi_docker_test

# Copy the requirements file to the working directory for cache purposes
COPY ./config/requirements.txt /fastapi_docker_test

# Install dependencies to my working directory:
RUN pip install -r requirements.txt

# Copy everything (except what is on the .dockerignore file) to the working directory 
COPY . /fastapi_docker_test

# Command to execute on the run
CMD ["python", "main.py"]