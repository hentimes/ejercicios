# Tarea 3 - Triagulos:

# Crear 4 triangulos rectangulos con altura/limite definitos
# por input ingresado por usuario.

N = int(input("Ingrese un valor: "))

# Imprime el primer triagunlo creciente
for i in range(1, N+1, 1):
  print ("*" * i)
print ("")

# Imprime segundo triangulo decreciente
for i in range(N, 0, -1):
  print ("*" * i)
print ("")

# Imprime tercer triangulo invertido creciente
for i in range(N):
  espacios = (N - i - 1)
  print (" " * espacios, end="")
  print ("*" * (i+1))
print ("")

# Imprime cuarto triangulo invertido decreciente
for i in range(N): # i = [0, 9]
  espacios = i  # [0, 9)
  asteriscos = N - i # [10, 1]
  print (" " * espacios + "*" * asteriscos)
  
