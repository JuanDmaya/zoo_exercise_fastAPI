from fastapi import FastAPI
from app.controllers.animal_controller import router as animalRouter

app = FastAPI()

app.include_router(animalRouter)