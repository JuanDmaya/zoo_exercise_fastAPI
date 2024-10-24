from fastapi import FastAPI, HTTPException 
from app.models.models import Animal, Mamifero, Ave
from app.services.services import AnimalService

app = FastAPI()

animal_service = AnimalService()

# Crear un nuevo animal
@app.post("/animales/")
def agregar_animal(animal: Animal):
    animal_service.agregar_animal(animal)
    return {"message": "Animal agregado correctamente."}

# Obtener todos los animales
@app.get("/animales/")
def obtener_animales():
    return animal_service.obtener_animales()

# Obtener un animal por nombre
@app.get("/animales/{nombre}")
def obtener_animal(nombre: str):
    animal = animal_service.obtener_animal_por_nombre(nombre)
    if animal:
        return animal
    raise HTTPException(status_code=404, detail="Animal no encontrado")

# Actualizar un animal
@app.put("/animales/{nombre}")
def actualizar_animal(nombre: str, animal_actualizado: Animal):
    actualizado = animal_service.actualizar_animal(nombre, animal_actualizado)
    if actualizado:
        return {"message": "Animal actualizado correctamente."}
    raise HTTPException(status_code=404, detail="Animal no encontrado")

# Eliminar un animal
@app.delete("/animales/{nombre}")
def eliminar_animal(nombre: str):
    eliminado = animal_service.eliminar_animal(nombre)
    if eliminado:
        return {"message": "Animal eliminado correctamente."}
    raise HTTPException(status_code=404, detail="Animal no encontrado")