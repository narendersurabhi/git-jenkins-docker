FROM python:3.8-slim

WORKDIR /app

# Copy the code into the container
COPY app.py .
COPY index.html .

# Install the required dependencies
RUN pip install Flask

EXPOSE 5050

# CMD ["python", "app.py"]
# ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0 --port=5000
ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0 --port=5050