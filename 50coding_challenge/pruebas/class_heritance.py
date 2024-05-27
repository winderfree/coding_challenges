import clase_prueba 
class estudiante(clase_prueba.Persona):
    def __init__(self, name, profesion) -> str:
       super().__init__(name)
       self.profesion = profesion
obj = estudiante("Jose","Informática")
obj2 = estudiante("Maria","Matemática")

print(f'nombre:{obj.name}, Profesión:{obj.profesion}')
print(f'nombre:{obj2.name}, Profesión:{obj2.profesion}')
 