# Tarea 3 - Triagulos:

# Crear 4 triangulos rectangulos con altura/limite definitos
# por input ingresado por usuario.

l = int(input("Ingrese un valor: "))
m = 0
"""
Manera poco efectiva de hacerlo.

for i in range(0, l):
  print ("*", end="")
print ("")
for j in range(l -1):
  print ("*", end="")
print ("")
"""

for i in range(l):
  i = (l - i)
  print ("*" * i)
print ("")

for j in range(l):
  j = (j + 1)
  print ("*" * j)
