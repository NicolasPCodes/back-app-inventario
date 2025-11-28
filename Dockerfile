# Usamos Python 3.13 (puedes cambiar a 3.12 si prefieres)
FROM python:3.13-slim

# Evita crear archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Evita usar buffer en logs
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalar dependencias del sistema si las necesitas
# RUN apt-get update && apt-get install -y build-essential

# Copia requirements
COPY ./app/requirements.txt .

# Instala paquetes
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu proyecto completo
COPY . .

# Exponemos puerto de Flask/FastAPI
EXPOSE 8000

# Comando por defecto para ejecutar la API
CMD ["python", "-m", "app.main"]