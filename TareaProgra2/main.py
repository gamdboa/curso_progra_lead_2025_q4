from cesar import encriptado_cesar, decriptrado_cesar
from vigenere import encriptado_vigenere, decriptrado_vigenere

def main():
    print("\n=== ENCRIPTADOR DANIEL G ===")
    text = input("\nIngrese el texto: ").lower()
    algorithm = int(input("Elija algoritmo, '1' para cesar, '2' para vigenere: "))

    if algorithm == 1:
        desplazado = int(input("Ingrese el desplazamiento (numero entero): "))
        action = int(input("Ingrese 1 para encriptar o 2 para desencriptar: "))

        if action == 1:
            result = encriptado_cesar(text, desplazado)
        elif action == 2:
            result = decriptrado_cesar(text, desplazado)
        else:
            print("Opción invalida.")
            return

    elif algorithm == 2:
        key = input("Ingrese la palabra clave (sin repetir letras): ").lower()
        action = int(input("'Ingrese 1 para encriptar o 2 para desencriptar: "))

        if action == 1:
            result = encriptado_vigenere(text, key)
        elif action == 2:
            result = decriptrado_vigenere(text, key)
        else:
            print("Opción inválida.")
            return
    else:
        print("Algoritmo invalido")
        return

    print(f"\nResultado: {result}")

if __name__ == "__main__":
    main()