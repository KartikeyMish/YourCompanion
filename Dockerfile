# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl

# Install Poetry using pip
RUN pip install poetry

# Copy the required files to the container's working directory
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root

# Copy the application code to the container
COPY . .

# Expose port 8080 to allow incoming traffic
EXPOSE 8080

# Set the environment variable for the OpenAI API key
ENV OPENAI_API_KEY=

# Start the FastAPI server
CMD ["uvicorn", "textbase.backend:app", "--host", "0.0.0.0", "--port", "8080"]
