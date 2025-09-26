encendido = False          # True = prendido, False = apagado
canal_actual = 1           # Canales válidos: 1-13
volumen_actual = 5         # Rango de volumen: 0-15

while True:
    print("\n--- MENÚ DEL TELEVISOR ---")
    print("1. Prender televisor")
    print("2. Apagar televisor")
    print("3. Subir volumen")
    print("4. Bajar volumen")
    print("5. Cambiar canal (1-13)")
    print("6. Imprimir estado")
    print("7. Salir   (también puede escribir «salir»)")
    
    opcion = input("Seleccione una opción: ").strip()

    # Permitir escribir «salir» o elegir 7 para terminar
    if opcion.lower() == "salir" or opcion == "7":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    # --- Prender televisor ---
    if opcion == "1":
        if not encendido:
            encendido = True
            canal_actual = 2
            print("Televisor encendido. Canal puesto en 2.")
        else:
            print("El televisor ya está encendido.")

    # --- Apagar televisor ---
    elif opcion == "2":
        if encendido:
            encendido = False
            print("Televisor apagado.")
        else:
            print("El televisor ya está apagado.")

    # --- Subir volumen ---
    elif opcion == "3":
        if volumen_actual < 15:
            volumen_actual += 1
            print(f"Volumen aumentado a {volumen_actual}.")
        else:
            print("Volumen ya está en el máximo (15).")

    # --- Bajar volumen ---
    elif opcion == "4":
        if volumen_actual > 0:
            volumen_actual -= 1
            print(f"Volumen disminuido a {volumen_actual}.")
        else:
            print("Volumen ya está en el mínimo (0).")

    # --- Cambiar canal ---
    elif opcion == "5":
        nuevo_canal = input("Ingrese canal (1-13): ").strip()
        if nuevo_canal.isdigit():
            nuevo_canal = int(nuevo_canal)
            if 1 <= nuevo_canal <= 13:
                canal_actual = nuevo_canal
                print(f"Canal cambiado a {canal_actual}.")
            else:
                print("Canal fuera de rango (1-13).")
        else:
            print("Entrada inválida: debe ser un número.")

    # --- Imprimir estado ---
    elif opcion == "6":
        estado = "ENCENDIDO" if encendido else "APAGADO"
        print("\n*** ESTADO DEL TELEVISOR ***")
        print(f"Potencia : {estado}")
        print(f"Canal    : {canal_actual}")
        print(f"Volumen  : {volumen_actual}")

    # --- Opción inválida ---
    else:
        print("Opción no reconocida. Intente de nuevo.")
