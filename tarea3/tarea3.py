# Tarea 3 - Triagulos:

# Crear 4 triangulos rectangulos con altura/limite definitos
# por input ingresado por usuario.

l = int(input("Ingrese un valor: "))
n = 0
"""
Manera poco efectiva de hacerlo.

for i in range(0, l):
  print ("*", end="")
print ("")
for j in range(l -1):
  print ("*", end="")
print ("")
"""

# Imprime el primer triagunlo creciente
for i in range(1, l+1, 1):
  print ("*" * i)
print ("")

# Imprime segundo triangulo decreciente
for i in range(l, 0, -1):
  print ("*" * i)
print ("")

# Imprime tercer triangulo invertido creciente
for i in range(l):
  espacios = (l - i - 1)
#  j = (j + 1)
  print (" " * espacios, end="")
  print ("*" * (i+1))
print ("")

# Imprime cuarto triangulo invertido decreciente
for i in range(l): # i = [0, 9]
  espacios = i  # [0, 9)
  asteriscos = l - i # [10, 1]
  print (" " * espacios + "*" * asteriscos)
  
