def fun1(param1: float,param2: float,param3: float,param4: float):
    return (param4-param2)/(param3-param1)
# print(fun1(4.1,2,66,9.5))

# lista=[1,6,99,123,444,0.5]
def fun2(lista: list):
    promedio=sum(lista)/len(lista)
    return promedio
# print(fun2(lista))

# lista=[1,6,99,123,444,0.5]
def fun3(lista: list):
    maximo=max(lista)
    minimo=min(lista)
    return maximo,minimo
# print(fun3(lista))

def fun4(lista: list):
    vocales=['a','e','i','o','u']
    for item in lista:
        temp=[]
        print(item)
        for letra in item:
            if letra in vocales:
                temp.append(letra)
        print(temp)
        
# lista=['hola','adios','alcaguete']
# fun4(lista)
