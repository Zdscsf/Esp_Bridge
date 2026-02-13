FROM python:3.11-slim

WORKDIR /app

COPY main.py .

RUN pip install pyserial

CMD ["python3", "main.py"]
