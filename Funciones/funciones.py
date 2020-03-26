"""
Se encarga de contener el cof¿digo necesario para realizar una tarea en especifico
la podemos utilizar n veces
"""
#para definir funciones usamos la palabre reservada def seguida del nombre y parentesis :
def saluda():
    print("Hola mundo")

#llamar funcion
saluda()
"""
Multiples valores
de entrada y salida
"""
def crear_mensaje(nombre):
    mensaje = "Hola {}, bienvenido al curso de python 3".format(nombre) #creamos el mensaje
    return mensaje #retorna el mensaje
    #asignamos un valor al parametro que tiene nuestra función
    #el valor se conoce como argumento

def suma(val1, val2, val3):
    return val1 + val2 + val3

def obtener_curso():
    return "Curso de Python", "Basico", 3.6

nuevo_mensaje = crear_mensaje("Miguel")
print(nuevo_mensaje)

resultado = suma(10, 20, 30)
print(resultado)

curso, nivel, version = obtener_curso()
print(curso, nivel, version)
"""
Refactor para reducir laslineas de codigo
def crear_mensaje(nombre):
    return "Hola {}, bienvenido al curso de python 3".format(nombre) #creamos el mensaje
    #asignamos un valor al parametro que tiene nuestra función
    #el valor se conoce como argumento
nuevo_mensaje = crear_mensaje("Miguel")
print(nuevo_mensaje)

def suma(val1, val2, val3):
    return val1 + val2 + val3
"""

"""
Recibir n cantidad de parametros
"""
def crear_usuario(nombre, apellido, edad):
    return{
    'nombre': nombre,
    'apellido': apellido,
    'nombre_completo': "{} {}".format(nombre, apellido),
    'edad': edad
    }

codi = crear_usuario("codi", "facilito", 6)

print(codi("nombre"))
print(codi("apellido"))
print(codi("edad"))

#podemos colocar valores por default a nuestros parametros
"""
REGLAS
la asignacion debe ser sin espacios
debe de comenzar de derecha a izquierda
no debe de haber saltos en nuestra aignación
"""
def valor_default(nombre=""): #pueden tener todos mis parametros un valor por default
    return nombre
valor_default()
