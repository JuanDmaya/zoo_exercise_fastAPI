from pydantic import BaseModel

class Animal(BaseModel):
    nombre: str
    edad: int
    especie: str

class Mamifero(Animal):
    periodo_gestacion: int

class Ave(Animal):
    puede_volar: bool
