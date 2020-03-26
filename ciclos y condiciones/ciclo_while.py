"""
while ejecutar n cantidad de veces hasta que una condicion deje de complirse
Algoritmo el cual nos permite saber cuantos digitos posee un numero
"""
numero = 123456789
contador = 0

while numero >= 1:
    #aumentar 1
    contador+= 1
    #en cada iteracion se reducira el numero
    numero = numero /10
    #disminuir 1
    ##contador-= 1
else:
    print ("La cantidad de digitos del numero es ", contador)
