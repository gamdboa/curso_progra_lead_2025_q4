# Haga un módulo que contenga una función que recibe una lista de "strings" y la función los imprime cada uno en una linea, concatenando un numero al inicio.
# Por ejemplo si recibe: 
# ["leer datos", "calcular desviacion estandard", "salir"]
# debe imprimir 

# 1. leer datos
# 2. imprimir desviacion estandard
# 3. salir 

# EXTRA: que lea la opción escogida por el usuario y valide si es valida (o sea que el número está entre 1 y 3), y si es válida, que la retorne. 

# Haga además un programa pequeño para probarlo y subalo a su folder de evidencia. 

lista_prueba=['una palabra','dos palabras', 'tras palabras']

def impre_lista(lista: list):
    eiffel=True
    print('Palabras disponibles:')
    for i in range(0,len(lista)):
        print(f'{i+1}. {lista[i]}')
    while eiffel:
        opcion=int(input('Ingrese un numero de los anteriores o seleccione -1 para salir: '))
        if opcion == -1:
            print('Ciao')
            break
        elif opcion < len(lista)+1:
            print(lista[opcion-1])
        elif opcion > len(lista):
            print('La opcion esta fuera del rango, intente de nuevo')
        
        
impre_lista(lista_prueba)