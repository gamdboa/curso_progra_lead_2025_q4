# Haga un modulo que haga funciones de cifrado. 
# El modulo debe tener 2 funciones: cifrar y descifrar. 
# Para cifrar, la función recibe 2 valores: un numero entero mayor de 1 (no valide, pruebe con numeros entre 1 y 10) y un texto. Luego usando el número realizará un cifrado usando el algoritmo de cifrado de cesar. Referencia: https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar
# Para descifrar, pues hace la operación inversa. Recibe un texto (cifrado) y el número y en convierte la letra cifrada en la original. 
# Asi, por ejemplo si mete al primero: 
# cifrar(1, "mario") deberia obtener "nbsjp"
# y para descifrar deberia llamar
# descifrar(1,"nbsjp") y obtener mario 
# NOTA: Cuando llega al Z si va para adelante seguiría la A. Y si llega a la A y sigue para atras, seguiría la Z. 

# Asuma el alfabeto inglés, sin ñ. 

palabra_prueba='alfabeto'
def cifrado(palabra: str,cifrado: int):
    cifrado=''
    crudo=palabra.lower()
    for caracter in palabra:
        print(caracter)
        if 'a' <= caracter <= 'z':
            car_nuevo=(ord(caracter)+cifrado)
            cifrado+=chr(car_nuevo)
    print(cifrado)
    
cifrado(palabra_prueba,1)

print(chr(ord('a')+1))