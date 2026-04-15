FROM python:3.14-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install uv globally
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies cleanly into system python for Docker
RUN uv pip install --system -r pyproject.toml

# Expose port and run server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
