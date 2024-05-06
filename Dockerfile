FROM python:3.11-slim
WORKDIR /app

COPY requrements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "server.py"]
