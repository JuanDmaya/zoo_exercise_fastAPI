from typing import List, Optional
from ..models.animal import Animal

class AnimalService:
    def __init__(self):
        self.animales: List[Animal] = []


    def agregar_animal(self, animal: Animal):
        self.animales.append(animal)

  
    def obtener_todos_los_animales(self) -> List[Animal]:
        return self.animales

    def obtener_animal_por_nombre(self, nombre: str) -> Optional[Animal]:
        for animal in self.animales:
            if animal.nombre == nombre:
                return animal
        return None

   
    def actualizar_animal(self, nombre: str, animal_actualizado: Animal) -> bool:
        for i, animal in enumerate(self.animales):
            if animal.nombre == nombre:
                self.animales[i] = animal_actualizado
                return True
        return False

    def eliminar_animal(self, nombre: str) -> bool:
        for i, animal in enumerate(self.animales):
            if animal.nombre == nombre:
                del self.animales[i]
                return True
        return False
