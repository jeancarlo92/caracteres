k=int(input("Ingrese numero de caracteres: "))
cad=input("Ingrese cadena: ")

cont=0
palabras=0
for caracter in cad:
   if caracter != ' ':
     cont+=1
     print(cont, caracter)
     if cont==k and cad[cont]==' ':
        palabras+=1
        cont=0
     #else:
     #    if cont==k:
     #       palabras+=1
   else:
      cont=0


print("Hay %d palabras con una longitud de %d caracteres " % (palabras, k ))
