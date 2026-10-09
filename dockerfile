FROM python:3.11-slim

WORKDIR /app

COPY requirements-1.txt .
RUN pip install -r requirements-1.txt

COPY . .

EXPOSE 5000

CMD ["python","app.py"]
