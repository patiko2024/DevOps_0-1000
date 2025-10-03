# Dockerfile
FROM python:3.10-slim

# Crear y usar directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY app.py .

# Instalar Flask
RUN pip install flask

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
