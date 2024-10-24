from fastapi import FastAPI
from .controllers import animal_controller

app = FastAPI()

app.include_router(animal_controller.router)
