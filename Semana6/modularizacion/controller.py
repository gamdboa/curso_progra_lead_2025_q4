import io_utils
import person_manager
import operaciones.date_validator as dv

def process(option):
    if option == 1:
        datos_persona = read_person_data()
        person_manager.store(datos_persona)
    elif option == 2:
        print_persons_data(person_manager.get_all_persons())
    else:
        print("opcion invalida.")

def read_person_data():
    data = []
    print("\n--- Ingreso de datos de persona ---")
    data.append(io_utils.read_str("Nombre: "))
    data.append(io_utils.read_str("Primer apellido: "))
    data.append(io_utils.read_str("Segundo apellido: "))
    data.append(io_utils.read_str("Direccion: "))
    data.append(io_utils.read_str("Fecha de nacimiento (YYYY-MM-DD): "))
    return data

def print_persons_data(list_of_data):
    for data in list_of_data:
        print(f"{data[0]} {data[1]} {data[2]}, de {data[3]}. {data[4]} ")
        if dv.validate(data[4]):
            print("la fecha es valida")
        else:
            print("la fecha es invalida")