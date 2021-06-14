# FizzBuzz
# Contar los numeros del 1 al 100
# Multiplo de 3 imprimir Fizz / Multiplo de 5 imprimir Buzz
# Multiplo de 3 y 5 imprimir FizzBuzz

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0: print ("FizzBuzz")
  elif i % 3 == 0: print ("Fizz")
  elif i % 5 == 0: print ("Buzz")
  else: print (i)


