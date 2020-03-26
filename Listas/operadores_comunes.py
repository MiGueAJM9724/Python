lista = [8.17, 90, 1, 5,  44, 1.32]
lista.sort() #ordena la lista de forma acendente
#lista.sort(reverse = True) ordena la lista de forma descendente
print(lista)
mayor = lista[0] #Para obtener el mayoy con ayuda de reverse, para obtener el menor solo con sort
#Tambien podemos apoyarnos de la funcion min o max
"""
mayor = max(Lista)
menor = min(lista)
longitud de nuestra lista
    longitud = len(lista)
    print(longitud)

Buscar elementos de nuestra lista
    resulta = 8.17 in lista #retorna True or False
Para obtener el indice
    indice = lista.index(8.17)
metodo count nos regresa un valor entero, nos muestra la cantidad de veces que
se encuentra el valor indicado
contador = lista.count(5)
"""
#Matrices
fila_uno = [10, 20]
fila_dos = [30, 40]
matriz = [fila_uno, fila_dos]

primer_elemento = matriz[0][0] #retorna 10
print(primer_elemento)
