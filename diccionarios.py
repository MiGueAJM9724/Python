"""
diccionarios nos permiten almacenar diferentes tipos de datos
son mutables podemos modificar su longitud, quitar elementos
no se rigen po la regla de los indices
coresponden a un llave y cada llave un valor
una llave puede ser cualquier tipo de dato
"""
diccionario = {}
diccionario = dict{}
#{llave: el valor el cual queremos asociar. }
diccionario = {"total": 55}
diccionario = {"total": 55, "descuento": True, "subtotal": 14}
#ejemplo 2
diccionario = {"total": 55, 10: "Curso de Python", (1, 2, 3): True}
#llaves

#un string ('total')
#un número entero (10)
#una tupla que almacena números enteros (1, 2, 3)
"""
podemos utilizar clases como llaves, el quivalente ne un json
 en python es un diccionario
 usuario = {
 'nombre': 'Nombre del usuairo',
 'edad': 23,
 'curso': 'Curso de Python',
 'skills':{
    'programcion': True,
    'base de datrs': False
    },
 'medallas': ['basico', 'intermedio']
 }
 """
#Creación del diccionario
diccionario = dict()
#agregar nueva llave valor
diccionario['usuario'] = 'eduardo'
#actuializar valor mediante una llaves
diccionario['usuario'] = 'eduardo_gpg'
#obtener el valor mediante una llave
print(diccionario['usuairo'])

#para obtener todas las llaves de nuestro diccionario utilizamos el metodo keys

>>> diccionario = {'eduardo': 1, 'Fernando': 2, 'uriel': 3, 'rafael': 4}
>>> diccionario.keys()
dict_keys(['eduardo', 'fernando', 'uriel', 'rafael'])
>>> diccionario.values()
dict_values([1, 2, 3, 4])
>>> for key, value in diccionario.items():
...     print(key, value)
...
Eduardo 1
fernando 2
uriel 3
rafael 4
# con el metodo get podemos establecer un valor por defaulft en dado0 caso no exista
#ejemplo

usuaerio = {
    'name': 'miguel Angel',
    'age': 23,
    'job': '__'
}
#se manda una lista vacia para que obtener un error
calificaciones = usuario.get('calificaciones', [])
if calificaciones:
    for calificaciones in calificaciones:
        print(calificacion)
#ejemplo convergation implimentando diccionario
usuarios = ['Eduardo', 'Fernando', 'Uriel', 'Rafael']
diccionario = {usuario: position + 1
                        for position, usuario in enumerate(usuarios)}
print(diccionario)
"""
Como funcionan los diccionarios
"""
diccionario_uno = {}
#agregar una llave con su valor
diccionario_uno["nombre"] = "codi" # codi se almacenara con la llave Nombre
valor = diccionario_uno["nombre"] #obtenemos un valor
diccionario_uno["nombre"] = 90

print(diccionario_uno)
print(valor)
#no pueden existir llaves duplicadas, por lo cual toma el ultimo valor asignado
diccionario_dos{"a":1, "b": 2, "c": 3, "a": 4}
print(diccionario_dos)

"""
Obtener elemnetos de un diccionario
"""
resultado_uno = diccionario["a"]
primnt(resultado_uno)
#si queremos verificar si una llave existe usamos la palabre reservada "in"
 resultado_uno = "a"  in diccionario_dos
 #uso del metodo get
 resultado = diccionario.get("z") #retorna none, nosotros podemos indicar un segundo valor
 #ejemplo
 resultado_uno = diccionario_dos.get("z", "La llave no existe")
 print(resultado_uno)
 #setdefault  si la llave existe nos retorna su valor, en caso la llave no existente se generara en el diccionarios

 resultado = diccionario.setdefault("z", [])
 print(diccionario_dos)

 """
 llaves, items y valores
 """

 #obtener todas las llaves de nuestro diccionario
 diccionario = {"a";1 , "b": 2, "c": 3}
  # nos retorna un objeto del tipo dict_keys, con todos los valores de nuestro c¿diccionarios
 resultado = diccionario.keys()
  # nos retorna un objeto del tipo dict_values, con todos los valores de nuestro c¿diccionarios
 resultado = diccionario.values()
   # nos retorna un objeto del tipo dict_, con todos los valores de nuestro c¿diccionarios
 resultado = diccionario.items()
 print(resultado)

#convertir a una tupla o lista
resultado = tuple(resultado)
"""
Eliminar elementos
"""
 diccionario = {"a";1 , "b": 2, "c": 3}
 #eliminar llave y su valores
 del diccionario["a"]
 #pop elimina la llave y su vALOR
 diccionario.pop()
 #eliminar todos los elementos
 diccionario = {}
 #clear
 diccionario.clear()
 print(len(diccionario)) #numnero de elementos
