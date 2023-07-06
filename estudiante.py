from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido_pat, apellido_mat, fecha_nacimiento, matricula, sexo, promedio):
        super().__init__(nombre, apellido_pat, apellido_mat, fecha_nacimiento, sexo)
        self.matricula = matricula
        self.promedio = promedio
        
    def imprimir_matricula(self):
        print(self.matricula)
        
    
    def __repr__(self):
        return "[{}] {}".format(self.matricula, self.nombre_completo())