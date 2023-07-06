class Persona:
    def __init__(self, nombre, apellido_pat, apellido_mat, fecha_nacimiento, sexo):
        self.nombre = nombre
        self.apellido_paterno = apellido_pat
        self.apellido_materno = apellido_mat
        self.fecha_de_nacimiento = fecha_nacimiento
        self.sexo = sexo
        
    def nombre_completo(self):
        return self.apellido_paterno + ' ' + self.apellido_materno + ', ' + self.nombre
    
    def __repr__(self):
        return self.nombre_completo()