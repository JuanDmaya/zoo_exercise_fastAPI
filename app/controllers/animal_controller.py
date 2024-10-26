from fastapi import APIRouter, HTTPException
from typing import List
from app.models.animal import Animal
from app.services.animal_service import AnimalService

router = APIRouter()
animal_service = AnimalService()


@router.post("/animales", response_model=str)
def agregar_animal(animal: Animal):
    animal_service.agregar_animal(animal)
    return "Animal agregado correctamente."

@router.get("/animales", response_model=List[Animal])
def obtener_todos_los_animales():
    return animal_service.obtener_todos_los_animales()


@router.get("/animales/{nombre}", response_model=Animal)
def obtener_animal_por_nombre(nombre: str):
    animal = animal_service.obtener_animal_por_nombre(nombre)
    if animal is None:
        raise HTTPException(status_code=404, detail="Animal no encontrado.")
    return animal

@router.put("/animales/{nombre}", response_model=str)
def actualizar_animal(nombre: str, animal_actualizado: Animal):
    actualizado = animal_service.actualizar_animal(nombre, animal_actualizado)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Animal no encontrado.")
    return "Animal actualizado correctamente."


@router.delete("/animales/{nombre}", response_model=str)
def eliminar_animal(nombre: str):
    eliminado = animal_service.eliminar_animal(nombre)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Animal no encontrado.")
    return "Animal eliminado correctamente."