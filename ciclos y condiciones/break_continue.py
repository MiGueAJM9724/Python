titulo = "Curso de python 3"
for caracter in titulo:
    if caracter == "p":
        continue # nos mostrara todos los caracteres menos la letra p hace que salte a la siguiente iteracion
        break # no se visualizaran los caracteres despues de p
    print(caracter) #imprime todos mis caracteres
