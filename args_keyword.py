def suma(val1, val2, val3):
    return val1 + val2 + val3
"""
funciones en las cuales no sabemos el numero de parametros a
Recibir en estos casos se usa un asterisco
"""
def suma_uno(*args):
    total = 0
    print(args) # es una tupla de los argumentos que asignamos
    for valor in args:
        total+=valor
    return total
"""
el uso del asterisco no nos limita a usar un tipo de dato, se recomienda simpre
usar el asterisco en el ultimo parametro, es recomendable si usamos el *
nombremos al parametro args

"""
def suma_dos(parametro_requerido, *args):
    total = 0
    total = 0
    print(args) # es una tupla de los argumentos que asignamos
    for valor in args:
        total+=valor
    return total
resultado = suma_dos("Este es un argumento requerido",10,20,30,50,20)
print(resultado)

"""
doble asterisco
nos agrupa los elementos en un diccionario
definimos funciones mas cloplejas
"""

"""
Formas de terminar una funciones
Va terminar cuando la ultima linea de codigo se ejecutada
Termina cuando se ejecute return, de lo contrario retornara none
"""

"""
Alcance global
globales pueden ser utilizadas dentro de funciones
}Para python las dos varibles son diferentes
"""
animal  = 'Leon' # variable global
def mostrar_animal():
    global animal  #modificar  la variable global dentro de la función
    animal = 'Ballena' #solo puede ser accedida dentro de la función variable local
    print(animal)
mostrar_animal()
print(animal)

"""
podemos asignar una función a una variable
Funciones Lambdas (funciones anonimas) todas retornan
algun valor, por lo cvual no se usa return
si queremos mas parametros los separamos por comas
"""
mi_funcion = lambda grados=0 : grados * 1.68 + 32 # funcion lambda


def centigrados_a_farhenheit(grados):
    return grados *1.8 +32

funcion_variable = centigrados_a_farhenheit
resultado = funcion_variable(32)
resultado = mi_funcion(32)
print(resultado)

"""
Estas son algunas formas en las cuales
podemos crear funciones lambdas más complejas.

sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : args[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)
"""

"""
Funciones map

En Python, la función map nos permite aplicar una función sobre los items de un
objeto iterable (lista, tupla, etc...).

Sintaxis
map(function, objeto iterable)

La función retornará un objeto map que posteriormente podemos convertir a una
lista o tupla.
def cuadrado(numero):
 return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)

lista_resultado = list(resultado)
print(lista_resultado)


Es posible utilizar map junto con una función lambda. En lo personal
considero esta la mejor opción.

lista = [1,2,3,4,5]
resultado = map(lambda numero: numero * numero , lista)

lista_resultado = list(resultado)
print(lista_resultado)
"""

"""
funciones anidadas

"""
def comenzar_play_list(lista):

    def reproducir(): #solo puede ser llamada dentro de la funcioón play list
        nomlocal lista# para modificar nuestra variable lista
        lista = [1,2,3]
        for val in lista: #hace uso del parametro lista
            print(val)
    reproducir()
    print(lista)
lista = ['track1', 'Track 2', 'Track3', 'Track4']
comenzar_play_list()

"""
Closures

"""
def mostrar_mensaje(mensaje):
    mensaje = mensaje.title() #nlocal

    def mostrar():
        print(mensaje)

    return mostrar

nueva_funcion = mostrar_mensaje("codigo facilito")
nueva_funcion()

"""
Decoradores
debemos de trabajar con 3 funciones por lo menos
a, b, c
a(b) -> c
"""
def decorador(funcion): #a
    def nueva_funcion(*args, **kwargs):
        print("podemos agregar codigo antes") #antes
        resultado = funcion(*args, **kwargs)
        print("podemos agregar codigo despues") #despues
        return resultado
    return nueva_funcion
    #pass #ciclos, condicionales por el momento nuestra funcion no realizara nada
@decorador
def funcion_a_decorar(): #b
    print("Esta es una función a decorar")

funcion_a_decorar()

@decorador
def suma(val1, val2):
    return val1 + val2

funcion_a_decorar()
print("\n")
resultado = suma(20,30)
print(resultado)


"""
Generador para la crear  de una secuencia de datos

"""
def table_multiplicar(numero, maximo=10):
    for posicion in range(1, maximo+1):
        yield numero * posicion, numero, posicion #retorna el resultado  sin terminar la función

for resultado, numero, posicion in table_multiplicar(9)
print(numero, "*", posicion, "= ", resultado)
