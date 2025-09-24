# Programa 1
trigger=True
lista=[]
while trigger:
    i = int(input('ingrese un numero entero:'))
    if i==1:
        trigger=False
        print('suma de numeros en lista: ',sum(lista))
    elif i%2==0:
        lista.append(i)
        print(lista)

# Programa 2
trigger=True
lista_par=[]
lista_imp=[]
while trigger:
    i = int(input('ingrese un numero entero:'))
    if i<0:
        trigger=False
        print('suma de numeros en lista par: ',sum(lista_par))
        print('suma de numeros en lista impar: ',sum(lista_imp))
    elif i%2==0:
        lista_par.append(i)
        print('numero par agregado: ',lista_par)
    elif i%2>0:
        lista_imp.append(i)
        print('numero impar agregado :',lista_imp)

# Programa 3
trigger=True
set1=set([])
counter=int(input('Ingrese un numero:'))
while trigger:
    counter-=1
    set1.add(str(input('Ingrese una palabra:')))
    if counter==0:
        trigger=False
        print('Elementos de Set:',set1)

# Programa 4
trigger=True
tupla=()
counter=int(input('Ingrese un numero:'))
while trigger:
    counter-=1
    tupla+=str(input('Ingrese una palabra:'))
    if counter==0:
        trigger=False
        print('Elementos de tupla:',tupla)

# # Programa 5
trigger=True
lista=[]
counter=5
while trigger:
    i = int(input('ingrese un numero :'))
    counter-=1
    lista.append(i)
    if counter==0:
        trigger=False
        print('Numero menor de la lista:',min(lista))
        print('Numero mayor de la lista:',max(lista))
        print('Lista:',lista)

# # Programa 6
trigger=True
lista=[]
counter=int(input('Ingrese un numero:'))
while trigger:
    counter-=1
    lista.append(str(input('Ingrese una palabra:')))
    if counter==0:
        trigger=False
        print('Palabra mas larga de la lista:',max(lista))
        print('Lista:',lista)
