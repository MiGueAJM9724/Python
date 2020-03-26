numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)

diccionario = {"a":1,"b":2}
for llave in diccionario:
    print(llave)

valores = ((10,20), ["String", "String"],(True,False))
for valor in valores:
    print(valor) # imprime todos mis valores de mi variable valores, junto con estructura
    #lista, tuplas


valores = ((10,20), ["String", "String"],(True,False))
for valor1, valor2 in valores:
    print(valor1, valor2) #solo me imprime los valores de los objetos
