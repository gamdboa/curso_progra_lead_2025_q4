from datetime import datetime, date

class Persona:

    def __init__(self, nombre, apellido1, apellido2, direccion, fecNac):
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._direccion = direccion
        self._fecha_nacimiento = fecNac

    def __str__(self):
        return f"{self._nombre} {self._apellido1} {self._apellido2} from {self._direccion}, nacio {self._fecha_nacimiento}"

    def __eq__(self,other): 
        if not isinstance(other, Persona):
            return false
        return self._nombre == other._nombre and self._apellido1 == other._apellido1 \
                and self._apellido2 == other._apellido2 and self._direccion == other._direccion \
                and self._fecha_nacimiento == other._fecha_nacimiento

    def __lt__(self, other): #si el self es menor que other. 
        if not isinstance(other, Persona):
            return false
        date1 = datetime.strptime(self._fecha_nacimiento, "%Y-%m-%d").date()
        date2 = datetime.strptime(other._fecha_nacimiento, "%Y-%m-%d").date()
        return date1 < date2
