FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container (optional)
COPY . .

# Define the default command (optional, adjust as needed)
# CMD ["python", "-m", "your_main_script"]
