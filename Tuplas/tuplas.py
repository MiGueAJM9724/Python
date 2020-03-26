"""
tuplas: son parecidas a las listas, la diferencia es que
las tuplas son inmutables (no se pueden modificar)
"""
tupla = ("Miguel", 2, 2.2, True)
tupla_uno = (1, 2, 3, 4, 5, 6, 7)
elemento = tupla[2] #retorna el valor 3
print(elemento)
"""
al igual que las listas se pueden hacer sub tuplas
"""
tupla_dos = (100, 200, 300, 400)
uno, dos, tres, cuatro = tupla
print(uno, dos, tres, cuatro)
"""
Cuando tratamos de asignar los valores alas varibles y nuestra tupla
contiene mas elementos, nos marcara un error, ya que quedan valores sin
asignar para solucionar esto se utiliza el * permitiendo asigar mas de un valor
a una varibles
tupla_dos = (1, 2, 3, 4, 5, 6)
uno, dos, tres, *cuatro = tupla
print(uno, dos, tres, cuatro) imprime 1 2 3 [4, 5, 6]
"""
#Comprimir y descomprimir tuplas
#la funcion zip nos va regresar un objeto de tipo zip, mas adelante se vera a detalle
tupla_tres = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]

resultado =zip(tupla_tres, lista, tupla_dos)
#resultado = tuple(resultado) #((1, 10), (2, 20), (3, 30), (4, 40))
resultado = list(resultado) #[(1, 10), (2, 20), (3, 30), (4, 40)]
print(resultado) #<zip object at 0x000001A24F5CB408>



#Desempaquetado de tuplas
"""
En ciertas ocasiones tendremos la necesidad de obtener algunos elementos de nuestras tuplas, por ejemplo, teniendo la siguiente tupla.

tupla = (10, 20, 30, 40, 50)
Necesito obtener el primero, el segundo y el último elemento; Para lograr esto tendremos un par de opciones; trabajando con índices y sin ellos. Veamos.

Si trabajamos con índices podemos hacerlo lo siguiente.

primero = tupla[0]
segundo = tupla[1]
ultimo = tupla[-1]
o simplemente podemos reducir las líneas de código y dejarlo en una sola.

primero, segundo, ultimo = tupla[0], tupla[1], tupla[-1]
La segunda opción es dejar de trabajar con las los índices y utilizar el guión bajo _.

primero, segundo, _, _, ultimo = tupla
Como observamos he colocado dos guiones bajos que hacen referencia a el número 30 y el número 40, valores que no necesitamos, por en de, no necesito almacenarlos en alguna variable; simplemente los ignoramos.

Ahora, que pasa si tengo una tupla mucho más grande y nuevamente necesito obtener esos tres elementos (el primero, el segundo y el último).

tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)
Lo que podemos hacer es utilizar el guión bajo _ junto con el asterisco * y aplicar lo que hemos visto anteriormente.

primero, segundo, *_, ultimo = tupla
De esta forma podemos trabajar de una forma más eficiente con las tuplas.
"""

#De listas a tuplas
lista_uno = ["Curso", "python", "Codigofacilito"]
tupla_cuatro = ["Introduccion", "Basico", "listas", "tuplas"]
#convertir tupla en lista
nueva_lista = list(tupla_cuatro)
print(nueva_lista)
#convertir lista en tuplas
nueva_tupla = tuple(lista_uno)
print(nueva_tupla)
"""
Los String pueden ser convertidos en listas y a tupla_dosejemplo
resultado
['E', 's', 't', 'e', ' ', 'e', 's', ' ', 'e', 'l', ' ', 'c', 'u', 'r', 's', 'o',
 ' ', 'd', 'e', ' ', 'P', 'Y', 'T', 'H', 'O', 'N']
('E', 's', 't', 'e', ' ', 'e', 's', ' ', 'e', 'l', ' ', 'c', 'u', 'r', 's', 'o',
 ' ', 'd', 'e', ' ', 'P', 'Y', 'T', 'H', 'O', 'N')
"""
mensaje = "Este es el curso de PYTHON"
nueva_list = list(mensaje)
nueva_tuple = tuple(mensaje)
print(nueva_list)
print(nueva_tuple)

#Resumen
