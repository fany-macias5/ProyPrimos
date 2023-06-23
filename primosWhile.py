#Alessandra Estefanía Robles Macías
try:
  n = int(input("Escribe un número: "))
except ValueError:
 n = 1
#De igual forma que en el código de for tuve que elimar unas líneas y modificarlas por otras solo que en este casao usando while
"""En este código me atore porque me decía que n no estaba definida, y no podía encontrar el error y después me di cuenta que en algun momento
había eliminado el valor de la variable n, en cuanto volví a escribirlo el programa ejecuto correctamente
"""
if n > 1:
    i = 2
    while i < n:
        if n % i == 0:
           print("NO")
           break
        i += 1
    else:
        print("SI")
else:
   print("NO")