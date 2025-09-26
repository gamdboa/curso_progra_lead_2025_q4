# Haga un programa que lea una lista de números enteros.
# Dicha lista será considerada como una función de choque de asteroides.
# El signo del numero indica la dirección: Si es positivo, va de derecha a izquierda, si es negativo va de izquierda a derecha.
# Cada vez que hay un positivo seguido de un negativo, o viceversa, hay un choque de asteroides.
# El “resultado” será la consecuencia de la suma de ambos. Y la lista resultante deberá decir: 0 si el asteroide no choco, o el resultado del choque EN EL MAYOR si lo hubo. 

# lista = [1,2,9,-5,-10]

def main():
    lista=leer_lista()
    asteroides(lista)

def leer_lista():
    str_lista=input('Ingrese una lista de numeros enteros separados por coma:')
    lista_cruda=str_lista.split(',')
    lista_procesada=[]
    for i in lista_cruda:
        lista_procesada.append(int(i))
    print(lista_procesada)
    return lista_procesada
    

def asteroides(lista: list):
    temp = []
    for indice in range(0, len(lista)-1):
        temp.append(procesar_pares(int(lista[indice]), int(lista[indice+1])))
    #[[0,-1], [0,1], [0,0]]
    result = []
    for pair in temp:
        if len(result) == 0:
            result.append(pair[0])
            result.append(pair[1])
        else:
            if pair[0] == pair[1] == 0:
                result.append(0)
            else:
                result.pop()
                result.append(pair[0])
                result.append(pair[1])
    print(result)
# def asteroides(lista: list):
#     resultado=[]
#     # i=0
#     for i in range(0,len(lista)-1):
#         a,b=lista[i],lista[i+1]
#         if a * b <0 and not (i+2<len(lista) and lista[i+1] * lista[i+2] <0):
#             suma=a+b
#             resultado[i if abs(a)>abs(b) else i+1]=suma
#         i+=1
#     return resultado

def procesar_pares(izq: int,der: int):
    if abs(izq) > abs(der) and izq*der<0:
        return [izq + der, 0]
    if abs(izq) < abs(der) and izq*der<0:
        return [0, izq+der]
    if abs(izq) == abs(der) or (izq > 0 and der >0) or (izq<0 and der<0):
        return [0,0]

main()