#Alessandra Estefanía Robles Macías
try:
  n = int(input("Escribe un número: "))
except ValueError:
  n = 1
#En este punto el programa corria pero primero me imprimia más de una vez si era un número primo, luego ya no imprimia nada
#Así que me puse a investigar un poco más de porque pasaba esto y también investigue un poco más sobre que funciones podría agregar al código
#Por lo que a partir de esta parte cambie varias cosas, hasta que el programa finalmente compilo de la forma que se requería
if n > 1:
   for i in range(2, n):
       if n % i == 0:
         print ("NO")
         break
   else:
    print("SI")
else:
    print("NO")