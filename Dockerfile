FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .
COPY .env .

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["python3", "main.py"]