# Stage 1: Build PostgreSQL database

# Copy initialization script
# COPY init.sql /docker-entrypoint-initdb.d/

# Stage 2: Build Django application
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /fitness_planner

# Copy the current directory contents into the container at /fitness_planner
COPY . /fitness_planner

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV POSTGRES_REMOTE_PORT=5432 \
    POSTGRES_REMOTE_HOST=db \
    POSTGRES_USERNAME=postgres \
    POSTGRES_PASSWORD=postgres \
    RELEASE_VERSION=${VERSION} \
    OPENSSL_CONF=/home/integration-proxy/openssl.cnf

# Expose port 8000
EXPOSE 8000

# Run Django migrations and start the server
CMD sh -c "python manage.py migrate && python manage.py create_sample_dataset && python manage.py runserver 0.0.0.0:8000"
