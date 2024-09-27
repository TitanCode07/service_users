from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.auth_user.utils import create_access_token
from app.auth_user.crud import get_user_by_email
from app.auth_user.security import verify_password
from app.auth_user.schemas import LoginSchema

def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Si las credenciales son correctas, generar el JWT
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
