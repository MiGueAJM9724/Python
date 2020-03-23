#
variable_uno = 10
variable_dos = 18
#operadores relacionales
mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos
#Nos retornan valores boooleanos
print(mayor) #false
print(menor) #true
print(mayor_igual) #false
print(menor_igual) #true
print(igual) #false
print(diferente) #true
#operadores logicos
#retornar valores booleanos
resultado = True and True and diferente
#resultado = True or True or diferente
result = not False
result_ = not True
print(resultado) #true
print(result) #true
print(result_) #false
