# creaciond el crud de users

from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .utils import get_password_hash

def create_user(db: Session, user: schemas.CreateUser):
    try:
        hashed_password = get_password_hash(user.password)
        db_user = models.User(
            username=user.username, 
            email=user.email, 
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print(e)


def get_users(db: Session, skip: int = 0, limit: int = 100):
     try:
        return db.query(models.User).offset(skip).limit(limit).all()
     except Exception as e:
        print(e)
def get_users_by_email(db: Session, email: str):
    try:
        return db.query(models.User).filter(models.User.email == email).first()
    except Exception as e:
        print(e)


def get_user_by_id(db: Session, user_id: int):
    try:
        return db.query(models.User).filter(models.User.id == user_id).first()
    except Exception as e:
        print(e)

def update_user(user_id: int, user: schemas.CreateUser, db: Session):
    try:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Actualiza los campos del usuario con los datos proporcionados
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        
        db.commit()
        db.refresh(db_user)  # Refresca la instancia para obtener los datos actualizados
        
        return db_user  # Devuelve el usuario actualizado

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error updating user")

def delete_user(db: Session, user_id: int):
    try:
        db.query(models.User).filter(models.User.id == user_id).delete()
        db.commit()
        return {"message": "User deleted successfully"}
    except Exception as e:
        print(e)


def find_user_by_id(user_id: int, db: Session):
    try:
        return db.query(models.User).filter(models.User.id == user_id).first()
    except Exception as e:
        print(e)