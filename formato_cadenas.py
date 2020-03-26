texto = "curso de python 3"
#nos retorna un nuevo String
#nos genera un nuevo Strin con la primera letra en mayuscula
resultado = texto.capitalize()
#resultado  = texto.swapcase() todas las letras en mayus las transformar en minuscula y viceversa
#resultado = texto.upper() todas las letras a mayusculas
#.lower() minusculas
print (resultado.isupper()) nos retornaran un booleano
#.islower()
#.tilte() #formato de titulo
texto.replace("python", "ruby", 1) #nos remplazo un valor en nuestro string el ultimo parametro nos indica el numero de veces a remplazar
print(rsultado)

#.strip()  retorna un nuevo string sin los espacios del inicio o al final


curso = "Python"
version = "3"
#resultado_dos ="curso de %s %s" %(curso, version) #%s nos asigna el valor de nuestra variable
resultado_dos = "curso de {} {}".format(curso, version) #nos regresan la misma salida
resultado_dos = "curso de {a} {b}".format(a = curso, b = version)
print(resultado_dos)
