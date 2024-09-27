from fastapi import FastAPI
from app.core.database import engine, SessionLocal
from app.users.models import Base
from app.users import routers
from app.auth_user import routes as auth_routers


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(routers.router)
app.include_router(auth_routers.router)


