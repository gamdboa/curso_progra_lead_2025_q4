nombres = []
apellidos1 = []
apellidos2 = []
direcciones = []
fechas_nacimiento = []

def store(data):
    nombres.append(data[0])
    apellidos1.append(data[1])
    apellidos2.append(data[2])
    direcciones.append(data[3])
    fechas_nacimiento.append(data[4])

def get_all_persons():
    data = []
    for pos, nombre in enumerate(nombres):
        one_person = []
        one_person.append(nombre)
        one_person.append(apellidos1[pos])
        one_person.append(apellidos2[pos])
        one_person.append(direcciones[pos])
        one_person.append(fechas_nacimiento[pos])
        data.append(one_person)
    return data