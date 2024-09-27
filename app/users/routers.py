# app/routes/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.users import controllers
from app.core.database import get_db
from app.users.schemas import CreateUser, User
from app.auth_user.utils import verify_jwt_token

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register", response_model=User)
def register(user: CreateUser, db: Session = Depends(get_db)):
    return controllers.register_user(user, db)

@router.get("/",response_model=list[User])
def get_users(db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    return controllers.get_users(db)


@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    return controllers.get_user_by_id(user_id, db)


@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, user: CreateUser, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    return controllers.update_user(user_id, user, db)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    return controllers.delete_user(user_id, db)