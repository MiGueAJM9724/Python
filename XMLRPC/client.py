#importamos el modulo ServerProxy
from xmlrpc.client import ServerProxy
#Crramos la conección a nuestro servidor
s = ServerProxy('http://localhost:20064', allow_none=True)
#usamos el metodo set de para guardar valores
s.set('lenguaje', 'python')
s.set('version', '3.7.7')
#retornamos las llaves almacenadas
s.keys()
#traemos los valores deacuerdo al parametro(llave)
s.get('version')
#Comprueba si existe o no dicha llave
s.exists('framework')
