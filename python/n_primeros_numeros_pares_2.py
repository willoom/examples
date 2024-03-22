n_pares = int(input('Números pares desde 2 que desea conocer: '))

acumulador=0
for i in range(0,n_pares):
  acumulador += 2
  print(acumulador)
