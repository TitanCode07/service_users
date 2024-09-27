# Usamos una imagen base de Python 3.10 slim
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos
COPY requirements.txt .

# Instalamos las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente de la aplicación
COPY . .

# Exponemos el puerto en el que corre FastAPI
EXPOSE 8001

# Comando por defecto para correr la aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
