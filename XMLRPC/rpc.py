#Importar el modulo de SimpleXMLRPCServer para poder usar XML-RPC
from xmlrpc.server import SimpleXMLRPCServer
#Clase que contendra los metodos para tyrabajar en nuestro servidor rpc
class RPC:
    _metodos_rpc = ['get', 'set', 'delete', 'exists', 'keys']
#funcion nos permitira inicializar nuestro servidor
    def __init__(self, direccion):
        self._datos = {}
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))
#Nos retorna los valores de acuerdo a su llave
    def get(self, nombre):
        return self._datos[datos]
#Nos permitira guardar los datos en un diccionario dentro de  nuestro servidor
    def set(self, nombre, valor):
        self._datos[nombre] = valor
#Nos permite eliminar los elementos
    def delete(self, nombre):
        del self._datos[nombre]
#Nos permite identificar si algun argumento  esta almecenado y nos devuelve
#true  o false
    def exists(self, nombre):
        return nombre in self._datos
#Metodo nos retorna las llaves de nuestro diccionario almacenado
    def keys(self):
        return list(self._datos)

    def iniciar_servidor(self):
        self._servidor.serve_forever()
#la condición nos permitira conectarnos a nuestro servidor a traves del puerto
#20064
if __name__ == '__main__':
    rpc = RPC(('', 20064))
    #mensaje al iniciar la API
    print('Se ha iniciado el servidor RPC')
    rpc.iniciar_servidor()
