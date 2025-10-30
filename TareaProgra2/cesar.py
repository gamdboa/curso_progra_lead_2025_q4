def encriptado_cesar(texto, desplazado):
    resultado = ""
    # descomponer letra por letra
    for char in texto:
        # reconoce solo letras
        if char.isalpha():
            # convertira posicion (0–25)
            posicion = (ord(char) - ord('a') + desplazado) % 26
            # convertir de vuelta a letra (usando como base el codigo de 'a')
            resultado += chr(posicion + ord('a'))
        else:
            resultado += char
    return resultado

def decriptrado_cesar(text, desplazado):
    # Solo se devuelve 1 posicion
    return encriptado_cesar(text, -desplazado)