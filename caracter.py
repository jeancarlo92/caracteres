k=int(input("Ingrese numero de caracteres: "))
cad=input("Ingrese cadena: ")

cont=0
palabras=0
for caracter in cad:
   if caracter != ' ':
     cont+=1
     print(cont, caracter)
   else:  
      if cont==k:
        palabras+=1
        cont=0
     else:
        cont=0
if len(cad)==k:
     palabras+=1
     print(palabras)
else:
  if cad[-k]!=' ' and cad[-k-1]==' ':
     palabras+=1
     print(palabras)


print("Hay %d palabras con una longitud de %d caracteres " % (palabras, k ))
