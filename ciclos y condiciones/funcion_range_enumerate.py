#range crea una secuencia de numeros los cuales los podemos iterar
for valor in range(10): #secuencia de 10 numeros
    print(valor) #0 al 9

"""
Podemos especificar de que numero comience la secuencia y hasta cual termine
for valor in range(1,20): #el numero 20 no se tomara en cuenta
    print(valor) #1 al 19

Se puede trabajar con numero snegativos
inclusive se puede colocar saltos
for valor in range(1, 101, 2): #el ultimo parametro es para der un salto de dos
    print(valor)# impreme puros numeros impares
Se puede convinar la funcion range con la funcion len
"""
lista = [1,2,3,4,5,6]
for indice in range(len(lista)):
    print("indice:", indice ,"valor:", lista[indice]) """
indice: 0 valor: 1
indice: 1 valor: 2
indice: 2 valor: 3
indice: 3 valor: 4
indice: 4 valor: 5
indice: 5 valor: 6
    """

    """
    enumerate
    Recorrer un objeto interable
    """
for indice, valor in enumerate(lista): # se puede indicar de que indice conmience
    #enumerate(lista, 10) el indice comensaria a contadel 10 al 15
    print("indice:", indice ,"valor:", valor) # mismo resultado del ejemplo anterior
