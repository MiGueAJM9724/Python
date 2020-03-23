#codigo duro hardcode      nombre = "Migue"
print("¿cual es tu nombre?")
#funcion input podemos leer lo que el usuario escribe con consola (valor string)
nombre = input()
#convier el string en tipo Int
print("¿cual es tu edad?")
edad = int(input())
print("¿cual es tu peso?")
peso = float(input())
#para que retorne un valor booleano
print("¿estas autorizado?")
autorizado = input() == "si"
#Para simplificar el codigo \n para dar un salto de linea, si no lo colocamos se
#escribiria en seguida de la pregunta
name = input("¿Cuál es tu nombre?\n")
print("Hola", nombre)
print("Edad:", edad)
print("Peso:", peso)
print("autorizado", autorizado)
