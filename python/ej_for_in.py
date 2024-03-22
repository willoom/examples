parejas = int(input('Introduce el número de parejas: '))


for vuelta in range (0,parejas):
  turno_ahora=""
  for j in range(1,parejas+1):
    if j==1:
      separador = ""
    else:
      separador = ", "
    if vuelta+j > parejas:
      nueva_pareja = vuelta + j - parejas
    else:
      nueva_pareja = vuelta + j
    turno_ahora = turno_ahora + separador + str(j) + "-" + str(nueva_pareja)
  print(turno_ahora)
