from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido_pat, apellido_mat, fech_nac, id_emp, sexo):
        super().__init__(nombre, apellido_pat, apellido_mat, fech_nac, sexo)
        self.id_empleado = id_emp

    def __repr__(self):
        return "[{}] {}".format(self.id_empleado, self.nombre_completo())