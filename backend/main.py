from fastapi import FastAPI
from auth import routes as auth_routes
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router)
