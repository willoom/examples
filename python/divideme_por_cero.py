dividendo = int(input('Introduzca el dividendo: '))
divisor = int(input('Introduzca el divisor: '))

try:
  cociente = dividendo / divisor
  resto = dividendo % divisor
  print('Dividir {0} entre {1} da un cociente de {2} y un resto de {3}'.format(dividendo, divisor, int(cociente), resto))
except:
  if divisor == 0:
    print('No podemos dividir por cero.')


