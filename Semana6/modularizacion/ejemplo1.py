# -*- coding: utf-8 -*-
"""
Programa simple de registro de personas.
No usa orientación a objetos ni funciones (más allá de main).
Cada atributo se guarda en una lista separada.
"""

def main():
    # Listas para almacenar los datos
    nombres = []
    apellidos1 = []
    apellidos2 = []
    direcciones = []
    fechas_nacimiento = []

    while True:
        print("\n" + "=" * 50)
        print("         MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Guardar datos de persona")
        print("2. Listar personas ingresadas")
        print("3. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            print("\n--- Ingreso de datos de persona ---")
            nombre = input("Nombre: ").strip()
            apellido1 = input("Primer apellido: ").strip()
            apellido2 = input("Segundo apellido: ").strip()
            direccion = input("Dirección: ").strip()
            fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ").strip()

            nombres.append(nombre)
            apellidos1.append(apellido1)
            apellidos2.append(apellido2)
            direcciones.append(direccion)
            fechas_nacimiento.append(fecha_nac)

            print("✅ Persona guardada exitosamente.")

        elif opcion == "2":
            print("\n--- Listado de personas ---")
            if len(nombres) == 0:
                print("No hay personas registradas.")
            else:
                for i in range(len(nombres)):
                    print("-" * 40)
                    print(f"Nombre completo : {nombres[i]} {apellidos1[i]} {apellidos2[i]}")
                    print(f"Dirección       : {direcciones[i]}")
                    print(f"Fecha nacimiento: {fechas_nacimiento[i]}")
                print("-" * 40)

        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
