# microservice-users
Este repositorio contendra un microservicio, realizado en el framework fastApi y se encargara de gestionar usuarios y su autenticacion



# Instalcion de docker


# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world


# Docker

docker run -d -p 8002:8000 --name "nombre-app" "nombre-app"

### imagen construida 

docker images

### borrar una imagen construida




1. Instalación de Docker

    Problema: Iniciar Docker y asegurarte de que se ejecute correctamente en tu sistema.
    Solución: Verifica que Docker esté instalado y en ejecución. Utiliza el comando sudo systemctl start docker para iniciar el servicio de Docker.

2. Configuración del Dockerfile

    Problema: Crear un Dockerfile para tu microservicio.
    Solución: Asegúrate de que el Dockerfile contenga las instrucciones correctas para construir tu imagen. Un ejemplo básico de un Dockerfile podría ser:

    dockerfile

    FROM python:3.10
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD ["python3", "app.py"]

3. Creación de la imagen

    Problema: Crear una imagen de Docker a partir del Dockerfile.
    Solución: Usa el comando:

    bash

    sudo docker build -t nombre_imagen .

4. Creación de un contenedor

    Problema: Crear un contenedor a partir de la imagen.
    Solución: Usa el comando:

    bash

    sudo docker run -d -p 8000:8000 nombre_imagen

5. Control de contenedores

    Detener un contenedor:
        Problema: Detener un contenedor en ejecución.
        Solución: Usa el comando:

        bash

    sudo docker stop id_contenedor

Iniciar un contenedor detenido:

    Problema: Reiniciar un contenedor que ha sido detenido.
    Solución: Usa el comando:

    bash

    sudo docker start id_contenedor

Eliminar un contenedor:

    Problema: Eliminar un contenedor que ya no necesitas.
    Solución: Usa el comando:

    bash

        sudo docker rm id_contenedor

6. Problemas de conexión a la base de datos

    Problema: Configurar la conexión de tu microservicio a PostgreSQL, que se ejecuta localmente.

    Solución: Asegúrate de que la dirección IP y el puerto estén correctamente configurados en tu microservicio. Utiliza la IP de tu máquina local (por ejemplo, 192.168.100.200).

    Errores comunes:
        Error de conexión: connection to server at "192.168.100.200", port 5432 failed: Connection refused.
            Solución: Verifica que PostgreSQL esté en ejecución y que la configuración de pg_hba.conf permita conexiones desde la IP del contenedor Docker.
        No pg_hba.conf entry for host:
            Solución: Asegúrate de que el archivo pg_hba.conf contenga una entrada que permita conexiones desde la dirección IP del contenedor, como:

            plaintext

            host    all             all             172.17.0.0/16          md5

7. Ejecución y depuración de contenedores

    Problema: Conectarse a un contenedor y ejecutar comandos.
    Solución: Usa el comando:

    bash

sudo docker exec -it id_contenedor bash

# postgresql

Paso 1: Editar postgresql.conf

    Localiza el archivo de configuración:
        El archivo de configuración de PostgreSQL generalmente se encuentra en la ruta /etc/postgresql/{version}/main/postgresql.conf en sistemas basados en Debian/Ubuntu, o en /var/lib/pgsql/{version}/data/postgresql.conf en sistemas basados en Red Hat/CentOS. Puedes encontrar la ruta exacta con el siguiente comando:

        bash

    sudo -u postgres psql -c "SHOW config_file;"

Edita el archivo:

    Abre el archivo postgresql.conf con un editor de texto, por ejemplo:

    bash

    sudo nano /etc/postgresql/{version}/main/postgresql.conf

Configura la dirección de escucha:

    Busca la línea que dice #listen_addresses = 'localhost' y cámbiala para que escuche en todas las interfaces (o especifica direcciones IP específicas). Por ejemplo:

    plaintext

        listen_addresses = '*'

        Esto permitirá que PostgreSQL escuche en todas las direcciones IP disponibles.

Paso 2: Editar pg_hba.conf

    Localiza el archivo pg_hba.conf:
        Este archivo también suele estar en la misma ruta que postgresql.conf. Usa un comando similar para encontrar su ubicación:

        bash

    sudo -u postgres psql -c "SHOW hba_file;"

Edita el archivo:

    Abre el archivo pg_hba.conf con un editor de texto:

    bash

    sudo nano /etc/postgresql/{version}/main/pg_hba.conf

Agrega una entrada para permitir conexiones externas:

    Agrega una línea al final del archivo para permitir conexiones desde un rango de direcciones IP. Por ejemplo, para permitir conexiones desde cualquier dirección IP en la red 192.168.1.0/24, agrega:

    plaintext

host    all             all             192.168.1.0/24          md5

Si deseas permitir conexiones desde cualquier IP, puedes usar:

plaintext

        host    all             all             0.0.0.0/0               md5

        Advertencia: Permitir conexiones desde cualquier IP (0.0.0.0/0) puede ser un riesgo de seguridad. Asegúrate de que esto sea necesario y que tu firewall esté configurado adecuadamente.

Paso 3: Reiniciar PostgreSQL

    Reinicia el servicio:
        Después de realizar los cambios, necesitas reiniciar el servicio de PostgreSQL para que los cambios surtan efecto. Usa el siguiente comando:

        bash

        sudo systemctl restart postgresql

Paso 4: Verificar la configuración del firewall

    Asegúrate de que el puerto de PostgreSQL (por defecto es el 5432) esté abierto en el firewall. Puedes usar ufw en Ubuntu para abrir el puerto:

    bash

    sudo ufw allow 5432/tcp

Paso 5: Probar la conexión

    Desde un cliente externo:
        Intenta conectarte a PostgreSQL desde un cliente externo usando la dirección IP del servidor y el puerto 5432. Por ejemplo:

        bash

psql -h [IP_DEL_SERVIDOR] -U [USUARIO] -d [NOMBRE_DB]

Asegúrate de que el usuario y la base de datos existen y que el usuario tiene permisos para acceder a la base de datos.


# medias a tomar en cuenta


l realizar el despliegue de contenedores en producción, hay varias medidas y consideraciones que debes tener en cuenta para asegurar que tus aplicaciones y bases de datos funcionen de manera eficiente, segura y confiable. Aquí tienes una lista de las principales:
1. Configuración de Seguridad

    Firewall: Asegúrate de que solo los puertos necesarios estén abiertos en el firewall del servidor. Por ejemplo, si tu aplicación usa el puerto 80 (HTTP) y 443 (HTTPS), abre solo esos puertos.
    Autenticación y Autorización: Implementa mecanismos de autenticación (como OAuth2, JWT) para asegurar que solo los usuarios autorizados puedan acceder a tu aplicación.
    SSL/TLS: Utiliza certificados SSL/TLS para cifrar el tráfico entre el cliente y el servidor, especialmente si transmites información sensible.

2. Gestión de Configuraciones

    Variables de Entorno: Usa variables de entorno para gestionar configuraciones sensibles (como credenciales de base de datos) en lugar de hardcodearlas en tu código.
    Archivos de Configuración: Utiliza archivos de configuración que puedan ser fácilmente modificados sin necesidad de recompilar la aplicación.

3. Persistencia de Datos

    Volumes de Docker: Usa volúmenes de Docker para almacenar datos de forma persistente. Esto es crucial para bases de datos que necesitan mantener su estado entre reinicios de contenedores.
    Backups Regulares: Implementa un sistema de backups regulares para tus bases de datos y otros datos críticos.

4. Monitoreo y Logging

    Monitoreo de Contenedores: Implementa herramientas de monitoreo (como Prometheus, Grafana) para rastrear el rendimiento de los contenedores y recursos del sistema (CPU, memoria, etc.).
    Logging Centralizado: Usa una solución de logging (como ELK stack - Elasticsearch, Logstash, Kibana) para recoger y analizar logs de diferentes servicios.

5. Redundancia y Escalabilidad

    Balanceadores de Carga: Si tu aplicación necesita manejar un alto volumen de tráfico, considera implementar un balanceador de carga para distribuir las solicitudes entre múltiples instancias de tu aplicación.
    Escalabilidad Horizontal: Diseña tu arquitectura para que pueda escalar horizontalmente (añadiendo más instancias de tus servicios) para manejar picos de tráfico.

6. Orquestación

    Docker Compose o Kubernetes: Considera usar herramientas de orquestación como Docker Compose o Kubernetes para gestionar el ciclo de vida de tus contenedores, incluida la escalabilidad, recuperación ante fallos y balanceo de carga.

7. Despliegue y Versionado

    Despliegue de Contenedores: Usa una estrategia de despliegue que minimice el tiempo de inactividad, como "blue-green deployments" o "rolling updates".
    Versionado de Imágenes: Etiqueta las imágenes de Docker con versiones específicas para evitar conflictos y facilitar la reversión si es necesario.

8. Pruebas

    Pruebas de Integración: Realiza pruebas exhaustivas para asegurar que todos los componentes de la aplicación funcionen bien juntos antes de desplegar en producción.
    Pruebas de Carga: Realiza pruebas de carga para evaluar cómo se comportará tu aplicación bajo diferentes niveles de tráfico.

9. Gestión de Recursos

    Limitaciones de Recursos: Configura límites de recursos para tus contenedores (CPU y memoria) para evitar que un contenedor consuma todos los recursos del servidor.
    Planificación de Recursos: Monitorea y ajusta los recursos según sea necesario basándote en el uso real y los requisitos de tu aplicación.

10. Consideraciones para Bases de Datos

    Separación de Servicios: Considera alojar tus bases de datos en un servidor separado del que ejecuta tus aplicaciones para mejorar la seguridad y el rendimiento.
    Conexiones a la Base de Datos: Configura las conexiones a la base de datos de forma adecuada, utilizando conexiones seguras y, si es posible, restringiendo el acceso a la base de datos solo a las IPs de tus contenedores.









. Creación de Clave Privada

Para generar una clave privada en formato PEM, puedes usar el siguiente comando de OpenSSL:

bash

openssl genrsa -out primary_key.pem 2048

Esto creará un archivo llamado primary_key.pem. Luego, puedes agregar esta clave al archivo .env de tu proyecto de la siguiente manera:

plaintext

# .env
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDmmQp0gVsyGt/4
CWOEDbMcd4GmezeBgdk2gAJ5M8JI0iXDXduBWF5oj6xDTm+RZaJStlzszVwYZXLI
4NMncg8W4feVzeQbe8+krcrR/a6QVpq6jRale5Cru27OJFm0rX67nfPO9l1FnlFU
gaumKS8/irgCv4RWS3gVBWK1nWGh3KNctCBXTT4TO144agpNFSBR+om+3mpGWbY6
whyll8X4BauICGmWPjsdlP5PsFP4W6k1iVzCiXQA6SRLMjJrTRsG6hchTLiOdJB0
UiKqTXHFwqx46Sk5BXTourp8aSmdicVfeGxLc3GHXWyEyLVeNYGhJMiNIry1+DYq
itb3hSStAgMBAAECggEAOHCf0vkwQXi7dcGShmk1/BMx+/XvlXabHBBDyreE537r
+D/aMHPZE52Kq6SggQVPsA/reZgf4Oa/q/P/KonrsI2ZJCTTHnj0zxksaa4+Ehzo
XR2YO+Oc+rNzAOh7vlGykags2uyI0rfXryfXw+ETq+k/dYi7ksWA/CAn00zUbyGT
N8wszC0i0gxKaqkml/paZtCqcH1LYq9Yr20iNo+BERFnDiv/pe3s/kBDn5LNAgJS
wS0CqqSLh0eN9J1PSy326edkI8rFZ67/1ISKcdt6D+CS684Hdhb7PRBiAjMwUiTE
ewp0pHfdAnUyFWCcrVlZYljHtGRbZfVdcKRcGa1J8QKBgQD0xW/vHLyllPx3zVYM
LDkPqaosOegqct78/B3dBLoAlhAKufdYP6v7FhWewqOv9B6lxa2WsNntXt14CBD4
oZ3q7rImxpXb49p+mt1BgOrTBIJkkteJerl2eBriuQZ1zEmvqmbnTYmLAlZZwfWJ
IzfisFmCnNApz5MxM4cuQjdr9QKBgQDxLScWpHdAeyG+ELCXnBvHGNP65wu/t/w6
2ShJwGxFtGY4npYDmygQa0HFbHgUVdWhgkN/Z87qbFcYH1wulZiWa/QkTMhyQak3
FToyWYtqBtUx9MjN1zwRp5JEnUdjINjxojieGwIIIByeOxfk2gsuzB3Cc+yovl8n
5n3HLKza2QKBgG4viun657kqTlSn7LpiFfXFDMQH9UlWmKcN32ulOw4Uf3g0qvHh
B8xp7qWfPQxyOnGpgTE6v3+pmszz5J/oMSyW8z+dWcy4z5z6netk21DO0NvxdnF+
+4onGwNBA3V31xvq+5PYRbh7/t88/wkS/49ej4zKhrKrrLkTVyEt0cEZAoGBALE3
yZpEvfAeypucLfcp2euB3fpnHmYBbxFbEtSm1aiet+Jw/bCmqVjvR4QngVEIBZPJ
YYnUIOJ3O8RY/uaoPFiD+QFXfo8empYEPiBTVjNR1AUCZy+CMfyTEtLic1tu/psH
5eyf0e1gk0beC1+5rS/1AwUpI8SXJtrt7oyV0mp5AoGAJ/UFBVBxDX7UlBS3d+Nq
ZxC+7Nk63G1aGbNQkeMezhtzG1oMG6Wn6C6BWpbg74lkIcIgIcEJHhkrwPaCgKnw
8/gOI7bUI0u4ryFu/rFI0lJcsWbUB6Os9L0caBOAL7gNQWrNWG7tuFSGkK3G4PIi
UuO4Ah7ksnEn3NkXwepPg0Q=
-----END PRIVATE KEY-----"

2. Configuración de Variable de Entorno

En tu archivo docker-compose.yml, puedes agregar la variable de entorno de la siguiente manera:

yaml

version: '3.8'

services:
  user_service:
    build: ./microservice-users
    ports:
      - "8001:8001"
    environment:
      - PRIVATE_KEY=${PRIVATE_KEY}  # Carga la clave privada desde .env
    networks:
      - app-network

Esto permitirá que tu aplicación acceda a la clave privada de forma segura.
3. Creación de Clave Pública

Para crear la clave pública a partir de la clave privada, usa el siguiente comando:

bash

openssl rsa -in primary_key.pem -pubout -out public_key.pem

Luego, puedes copiar la clave pública en el contenedor de tu API Gateway mediante el Dockerfile.
4. Configuración del Dockerfile

Tu Dockerfile para el API Gateway puede verse así:

dockerfile

FROM nginx:latest

# Copia la clave pública al contenedor
COPY public_key.pem /etc/ssl/certs/

# Copia tu archivo de configuración nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Otros comandos que necesites

5. Integración con NGINX

Ya tienes configurado NGINX para funcionar como API Gateway. Tu archivo nginx.conf puede verse así:

nginx

worker_processes auto;

events {
    worker_connections 1024;
}

http {
    upstream user_service {
        server user_service:8001;  # Asegúrate de que el puerto es correcto
    }

    upstream finance_service {
        server finance_service:8000;  # Asegúrate de que el puerto es correcto
    }

    server {
        listen 80;

        location /users/ {
            proxy_pass http://user_service;  # Proxy hacia el servicio de usuarios
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /finance/ {
            proxy_pass http://finance_service;  # Proxy hacia el servicio de finanzas
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location / {
            auth_jwt "Protected";
            auth_jwt_key_file /etc/ssl/certs/public_key.pem;  # Aquí es donde se utiliza la clave pública
        }
    }
}

6. Configuración de NGINX-JWT

Asegúrate de que el módulo nginx-jwt esté instalado y configurado para verificar el JWT en el API Gateway.
7. Estructura del docker-compose.yml

Tu archivo docker-compose.yml debería verse como sigue, integrando todos los servicios:

yaml

version: '3.8'

services:
  user_service:
    build: ./microservice-users
    ports:
      - "8001:8001"
    environment:
      - PRIVATE_KEY=${PRIVATE_KEY}
    networks:
      - app-network

  finance_service:
    build: ./insurance-market-statistics
    ports:
      - "8000:8000"
    networks:
      - app-network

  api_gateway:
    build: ./api_gateway  # Asegúrate de tener un Dockerfile en esta carpeta
    volumes:
      - ./api_gateway/nginx.conf:/etc/nginx/nginx.conf
      - ./api_gateway/public_key.pem:/etc/ssl/certs/public_key.pem
    ports:
      - "80:80"
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

Este archivo asegura que todos los microservicios estén en la misma red y que las configuraciones sean correctas.
Resumen Final

Estos pasos te proporcionan una guía completa para la implementación de un API Gateway utilizando NGINX, autenticación JWT, y asegurando que las claves se manejen de forma segura dentro de contenedores Docker. Si necesitas más detalles en algún paso o un ejemplo específico, no dudes en preguntar.