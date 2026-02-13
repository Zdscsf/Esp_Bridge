FROM python:3.11-slim

# Installer pyserial
RUN pip install pyserial

# Copier le script dans le container
WORKDIR /app
COPY main.py .

# Lancer le script
CMD ["python3", "main.py"]
