from pydantic import BaseModel

class Animal(BaseModel):
    nombre: str
    edad: int
    especie: str
