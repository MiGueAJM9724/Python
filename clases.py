"""

"""
class Usuario:#Primera letra en mayuscula e identar

    def __init__(self, username='', email='', nombre=''):
        self.username = username
        self.email = email
        self.nombre = nombre

    def saluda(self)
    return "hola, soy un usuario" + self.nombre

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self)
    print(self.nombre)

codi = Usuario("codi", "codi@js", "codigo")
resultado.codi.saluda()
print(resultado)
        #para evitar el tipo de metodos y asignacion
    """def saluda(self, nombre):
        print("Hola soy un usuario" + nombre)

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self)
    print(self.nombre)
        #dentro de la clase atributos
    def crear_nombre(self, nombre):
        self.nombre = nombre
codi = Usuario() #intanciar (crear un objeto)
#fuera de la clase
codi.username = "codi"
codi.correo = 'codi@gmail.com'

facilito = Usuario()
facilito.username = "codi"
facilito.correo = 'codi@gmail.com'

#codi.saluda("codi")
facilito.saluda("facilito")
codi.mostrar_username()
facilito.mostrar_username()
codi.crear_nombre("codigo")
codi.mostrar_nombre()
print(type(codi))
print(codi.saluda("codi"))
"""

"""
Metodos funciones dentro de la clase, todos los metodos reciben un parametro,
en este caso self que hace referencia al objeto
"""

"""
Atributos
fuera de la clase y dentro de la clase
"""

"""
Tipos de atributos
variables de instancia y clase

"""
class Circulo:
    pi = 3.1415 #es una variable de clase y pueden ser utilizadas por instancias
    def __init__(self, radio):
        self.radio = radio #variable de instancia, no se comparten entre instancias

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circuilo_b.radio = 100

print(Circulo_a.pi)
print(circulo_a.radio)
print(circulo_b.radio)

"""
Metodos estaticos
los podemos utilizar sin necesidad de hacer una instancia
"""

class Triangulo:
    def area(self):
        return (self.base * self.altura) / 2
triangulo = Triangulo() #instancia
triangulo.base = 10
triangulo.altura = 20

resultado = triangulo.area()
print(resultado)

"""
Sin instancias
"""
class Triangulo:
    @staticmethod
    def area(base, altura):
        return (self.base * self.altura) / 2

resultado = Triangulo.area(10,20)

print(resultado)


"""
Meyodos de Clase
"""
class Circulo:
    pi = 3.1416

    def area(cls, radio):
        return(cls): #no es reservada, pero por convencion se usa, y hace referencia a la clases
        return cls.pi*radio**2

resultado = Circulo(10)
print(resultado)

"""
Herencia
Nos permite crear clases con clases existentes, reutilizar y reducir codigo

"""

class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("durmiendo")

    def comun(self):
        print("Este es un metodo de animal")
#heredamos de la clase animal  las funciones comer y dormir
#animal es una clase padre
class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha

    def comun(self):
        print("Este es un metodo de mascota")
#multiple herencia
class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombremos

    def ladrar(self):
        print("ladrando")

    def comun(self):
        print("Este es un metodo de perro
#sobre escritura de metodos
    def dormir(self):
        print(self.nombre, "Esta durmiendo")
        Animal.dormir(self)
        print("No molestar")

class Gato(Animal):
    def ronronear(self):
        print("ronroneo")



firulais = Perro("firulais")
firulais.comer()
firulais.dormir()
firulais.ladrar()
firulais.comun()
firulais.fecha_adopcion("hoy")
bola_de_nieve = Gato()
bola_de_nieve.comer()

"""
Herencia multiple
Las clases que heredemos deben colocarse en la parte superior, de lo contrario
nos marcara como no definida

Que paso si tienen un metodo en comun (mismo nombre)
Busca el metodo comun enla clase principal en este caso perro
Orden de busqueda
primero de izquierda a derecha
"""


"""
Sobre escritura de Metodos (override)

"""

"""
clase object
"""
#proimera forma de crear clase gato hereda del clase object
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

#segunda forma
class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre

gato = Gato("Bigotes")
pato = Pato("Lucas")
pato.edad = 6
print(gato) #retorna su direccion en memoria, para no visualizar la direccion en memoria
# utilizamos str, ahora vizualizaremos el nombre
print(pato.__dict__) #retorna un diccionario
