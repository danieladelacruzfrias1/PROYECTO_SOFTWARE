# Usa una imagen base de Python con las dependencias necesarias para Tkinter
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo .py y cualquier otro necesario en el contenedor
COPY . /app

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "./Notas.py"]
