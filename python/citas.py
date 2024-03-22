n_parejas = int(input('Intruduzca el número de parejas: '))

for i in range(0,n_parejas):
  turno = ""
  for j in range(0,n_parejas):
    emparejamiento = str(j+1)+"-"+str((j+i)%n_parejas + 1)
    if (j!=0):
      turno += ", "
    turno += emparejamiento
  print (turno)
