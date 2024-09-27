from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from app.core.database import get_db


# registro de usuarios
def register_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user_email = crud.get_users_by_email(db, user.email)
    if db_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)


# Obtiene todos los usuarios
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

def update_user(user_id: int, user: schemas.CreateUser, db: Session):
    db_user = crud.find_user_by_id(user_id, db)  # Asegúrate de que esta función esté bien implementada
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.update_user(user_id, user, db)

def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.find_user_by_id(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db, user_id)