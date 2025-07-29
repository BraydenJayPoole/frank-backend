# Version of the Docker Compose file format
version: '3.8'

# Defines the services (containers) that make up our application
# References: 1.2. System Architecture & Implementation Plan
services:
  # The FastAPI application service
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000" # Maps port 8000 on the host to port 8000 in the container
    volumes:
      - ./app:/app # Mounts the local 'app' directory into the container for live reloading
    env_file:
      - .env # Loads environment variables from the .env file
    depends_on:
      - db
      - redis
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  # The PostgreSQL database service
  db:
    image: postgres:15-alpine # Uses the official PostgreSQL 15 image
    volumes:
      - postgres_data:/var/lib/postgresql/data/ # Persists database data
    env_file:
      - .env # Loads database credentials from the .env file
    ports:
      - "5432:5432" # Exposes the database port for local connections if needed

  # The Redis service for caching and message broking
  redis:
    image: redis:7-alpine # Uses the official Redis 7 image

  # The Celery worker service for background tasks
  celery:
    build:
      context: .
      dockerfile: Dockerfile
    command: celery -A app.celery_worker.celery worker --loglevel=info
    volumes:
      - ./app:/app
    env_file:
      - .env
    depends_on:
      - redis

# Defines the named volume for persisting PostgreSQL data
# This ensures your data is not lost when containers are stopped and started.
volumes:
  postgres_data:
