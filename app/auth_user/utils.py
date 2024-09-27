import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


security = HTTPBearer()


# Leer la clave privada desde la variable de entorno
SECRET_KEY = os.getenv("PRIVATE_KEY")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")
if(SECRET_KEY is None):
    SECRET_KEY = "secret"

ALGORITHM = "RS256"  # Asegúrate de usar el algoritmo correcto
ACCESS_TOKEN_EXPIRE_HORAS = 4

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HORAS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        # Decodificar el token usando la clave pública
        payload = jwt.decode(credentials.credentials, PUBLIC_KEY, algorithms=["RS256"])
        return payload  # Devuelve el payload si es válido
    except jwt.JWTError:
        # Si el token no es válido, lanza una excepción
        raise HTTPException(status_code=401, detail="Invalid or expired token")