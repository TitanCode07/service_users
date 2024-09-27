from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.auth_user.controllers import authenticate_user
from app.auth_user.schemas import LoginSchema, Token

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/login", response_model=Token)
def login(loginData: LoginSchema, db: Session = Depends(get_db)):
    return authenticate_user(loginData.email, loginData.password, db)