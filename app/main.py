from fastapi import FastAPI

from .api.v1.routers import weather_router

app = FastAPI()


app.include_router(weather_router, prefix="/api/v1")
