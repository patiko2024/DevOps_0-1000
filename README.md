# DevOps_0-1000
La tarea consiste en:
Crear una pequeña aplicación web en Python que:
1.	Se ejecute dentro de un contenedor Docker.
2.	Use variables de entorno que se definan en docker-compose.
3.	Monte un volumen donde se escriba un archivo.
4.	Muestre un "Saludo" en el navegador en un puerto accesible (por ejemplo, localhost:5000).
________________________________________
Estructura:
app/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── .env
└── data/             # Carpeta para el volumen (se creará automáticamente)
________________________________________
Usamos 
Flask, un microframework web en Python
Resumen 
1.	Python + Flask ejecutan una app que responde en el puerto 5000.
2.	Se lee una variable de entorno (NOMBRE) definida en .env.
3.	Se Escribe un archivo dentro de un volumen.
4.	Dockerfile empaqueta la app.
5.	Docker Compose gestiona todo: construcción, variables, puertos y volumen.
6.	Tú accedes desde tu navegador a localhost:5000.
