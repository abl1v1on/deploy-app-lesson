FROM python:3.12-slim

WORKDIR /app/backend

COPY requirements.txt /app/backend/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "main.py"]
