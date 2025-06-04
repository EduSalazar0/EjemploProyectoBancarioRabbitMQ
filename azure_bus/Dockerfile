# Imagen base
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto (puedes sobreescribirlo en docker-compose)
CMD ["python", "-m", "azure_bus.producer.send_transaccion"]
