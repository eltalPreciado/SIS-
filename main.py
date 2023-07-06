
from estudiante import Estudiante
from profesor import Profesor
from persona import Persona

persona = Persona("María", "González", "Pérez", "1994-01-01", "f")
estud1 = Estudiante("Gerardo", "Mathus", "Gómez Sandoval",
                    "1994-01-24", "2301142", "m", 9.8)
prof1 = Profesor("Isaac", "Newton", "Pérez", "1643-01-04", "P123123", "m")

print(prof1)
print(estud1)
print(estud1.promedio)

estud1.imprimir_matricula()