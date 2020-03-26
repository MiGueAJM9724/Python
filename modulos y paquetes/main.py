#import modulos
from modulos import *
#utilizamos suma del modulo modulos
#resultado = modulos.suma(10, 20)
resultado = suma(10, 20)
print(resultado)

"""
Formas de imports
from modulos import * #importamos todo
from modulos import (suma,
                    resta) as nueva_suma #podemos renombrar el modulo y podemos dar saltos
                    de linea si son mucho metodos
from modulos inport suma, resta, multiplicacion # si utilizamos esta forma ya no debemos especificar modulos.suma
# ya solo con suma
"""

"""
al importar
Archivos PYC se generan nuevos archivos folder (__pycache__), que contiene un archivo compilado
"""

"""
Atributo __name__
"""
import modulos
dir(modulos) #retorna una lista con todos los objetos de nuestro modulo
print(modulos.__name__) #muestra el nombre del modulo
print(__name__) #__main__
