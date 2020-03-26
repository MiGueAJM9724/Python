curso = "Curso de Python"
curso = "c" + curso[1:] + str(3) + " " + "codigo facilito"
#str nos transforma cualquier tipo de dato a string
"""
si solo colocamos un valor
entero o otro nos marcaria error
"""
#genera un nuevo string con c minuscula

"""
Busqueda de cadenas
"""
mensaje = "este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
rezultado = mensaje.count("e") # nos retorna el numero de veces de caracter o palabra que buscamos
# otro forma es usar in
resultado = "texto" in mensaje # nos regresa un valor booleamo podemos negarlo haciendo uso de not in
#otro metodo
resultado = mensaje.find("texto") #nos regresa un entero, (posicion en la que se encuentra la letra t de texto)
resultado = mensaje[resultado: resultado + len("texto")] # nos retorna texto dada la posicion de resultado con el metodo find
print(resultado)

#startswith("este") para identificar si un string se encuentra al principio de nuestra cadena de texto
#endwith() nos retorna un valor booleano, si un string se encuentra al final de nuestro texto
