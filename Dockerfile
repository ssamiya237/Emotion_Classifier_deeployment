# Use a slim Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for gunicorn
EXPOSE 8080

# Start the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
