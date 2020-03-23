#Listas: estructura de datos; estructura: nombre de la variabl, signo igual, corchetes
lista = ["Migue", 10, True, 24.97]
"""
diferencia de listas y arreglos
Cambian de tamaño en tiempo de ejecuacion y pueden modificar los elementos
almacenados en ellas
"""
cursos = ["python", "php", "kotlin", "swift", "java", "c#", "javascript"]
#curso = cursos[2]  //kotlin
curso = cursos[-1]  #javascript
print(curso)
# Se pueden generar sublistas a partir de estas
#ejemplo
#sub = cursos[:5] identifica que queremos que inicie desde indice 0
#sub = cursos[3:] identifica que queremos todos los valores despues del indice 3
#sub = cursos[:] nos retorna todos los valores
"""
sub = cursos[0:6:2] Con las sublistas podemos obtener los elementos mediante saltos
resultado es python swift javascript

tambien podemos obtener el inverso de nuestra lista de la siguiente manera
sub = cursos[::-1]
"""
sub = cursos[0:3] # puedes iniciar desde cualquier indice
print(sub)

"""
Sub listas
Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a
 partir de otra.

[:] Todos los elementos.
[start:] Todos los elementos desde el índice establecido(start).
[:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
[start:end] Todos los elementos de un rango de índices.
[start:end:step] Todos los elementos de un rango de índices con saltos.
De igual forma, este listado es aplicable a las tuplas y los strings.

Resumen del bloque listas

Las listas cuentan con una gran cantidad de metodos, algunos son
lista.count()
lista.append()
lista.insert()
lista.remove()
lista.index()
lista.clear()
lista.sort()

trabajamos modelos con n dimensiones
"""
