def encriptado_vigenere(texto, clave):
    resultado = ""
    largo_clave = len(clave)
    for i, char in enumerate(texto):
        # reconoce solo letras
        if char.isalpha():
            # calcular deplazamiento de clave
            desplazado = ord(clave[i % largo_clave]) - ord('a')
            # desplazamiento
            pos = (ord(char) - ord('a') + desplazado) % 26
            resultado += chr(pos + ord('a'))
        else:
            resultado += char
    return resultado


def decriptrado_vigenere(texto, clave):
    resultado = ""
    largo_clave = len(clave)
    # enumerate() nos da un contador (i) y la letra actual (char)
    for i, char in enumerate(texto):
        if char.isalpha():
            # Calculamos cuánto hay que "desplazar" la letra
            desplazado = ord(clave[i % largo_clave]) - ord('a')
            # char se convierte a numero y resta el desplazamiento (lo que se movio inicialmente)
            # se usa % 26 para que el conteo sea circular (de 'a' a 'z')
            pos = (ord(char) - ord('a') - desplazado) % 26
            resultado += chr(pos + ord('a'))
        else:
            resultado += char
    return resultado