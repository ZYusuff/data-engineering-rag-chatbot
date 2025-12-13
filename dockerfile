# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file & install dependecies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY /frontend .
COPY api.py .
COPY function_app.py .

# Expose ports
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
