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
    for i, char in enumerate(texto):
        if char.isalpha():
            desplazado = ord(clave[i % largo_clave]) - ord('a')
            pos = (ord(char) - ord('a') - desplazado) % 26
            resultado += chr(pos + ord('a'))
        else:
            resultado += char
    return resultado