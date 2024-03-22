n_parejas = int(input('Intruduzca el número de parejas: '))

for i in range(0,n_parejas):
  turno = ""
  for j in range(1,n_parejas+1):
    chico = j
    chica = j+i
    if chica>n_parejas:
      chica -= n_parejas
    emparejamiento = str(chico)+"-"+str(chica)
    if (j!=1):
      turno += ", "
    turno += emparejamiento
  print (turno)
