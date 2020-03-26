curso = "Curso de Python 3"
resultado= len(curso)
print(resultado) #numero de caracteres en variable curso
"""
una vez conocido el numero de caracteres podemos navegar
entre ellos mediante el indice
"""
resultado = curso[1:16:2]
print(resultado)

#trabajo de string como listas

lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#, C; C++;"
separador = "; "
resultado = lenguajes.split(separador) #['Python', 'Java', 'Ruby', 'PHP', 'Swift', 'JavaScript', 'C#, C', 'C++;']
#resultado = lenguajes.split("; ") #['Python', ' Java', ' Ruby', ' PHP', ' Swift', ' JavaScript', ' C#, C', ' C++', '']
#resultado = lenguajes.split() #['Python;', 'Java;', 'Ruby;', 'PHP;', 'Swift;', 'JavaScript;', 'C#,', 'C;', 'C++;']
""""
retorna una nueva lista apartir del texto que hemos utilizado
el texto es dividido mediante un separador
por defautl es un espacio
"""
print(resultado) #resultado es una lista
#convertir la lista en un string
nuevo_string = " ".join(resultado) #retorna un String
print(nuevo_string)
#Python Java Ruby PHP Swift JavaScript C#, C C++;
nuevo_string_ = separador.join(resultado)
print(nuevo_string_)
#Python; Java; Ruby; PHP; Swift; JavaScript; C#, C; C++;
"""
Cuando nuestro string contenga saltos de linea
"""
texto = """Texto
con saltos
de linea"""
resultado_ = texto.splitlines()
print(resultado_)
#['Texto', 'con saltos', 'de linea']
