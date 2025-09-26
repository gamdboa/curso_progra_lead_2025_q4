import modules as m

def main():
    while True:
        m.print_menu()

        opcion = input("Seleccione una opción: ").strip()

        # Permitir escribir «salir» o elegir 7 para terminar
        if opcion.lower() == "salir" or opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        m.process_option(opcion)

main()