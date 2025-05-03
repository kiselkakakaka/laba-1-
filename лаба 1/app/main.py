
from fastapi import FastAPI
from app.routes import users, auth_routes

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth_routes.router, tags=["auth"])
