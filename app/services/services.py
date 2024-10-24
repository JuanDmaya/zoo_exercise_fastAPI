from typing import List, Optional
from app.models.models import Animal

class AnimalService:
    def __init__(self):
        self.animales: List[Animal] = []

    def agregar_animal(self, animal: Animal):
        self.animales.append(animal)

    def obtener_animales(self) -> List[Animal]:
        return self.animales

    def obtener_animal_por_nombre(self, nombre: str) -> Optional[Animal]:
        for animal in self.animales:
            if animal.nombre.lower() == nombre.lower():
                return animal
        return None

    def actualizar_animal(self, nombre: str, animal_actualizado: Animal) -> bool:
        for idx, animal in enumerate(self.animales):
            if animal.nombre.lower() == nombre.lower():
                self.animales[idx] = animal_actualizado
                return True
        return False

    def eliminar_animal(self, nombre: str) -> bool:
        for animal in self.animales:
            if animal.nombre.lower() == nombre.lower():
                self.animales.remove(animal)
                return True
        return False
