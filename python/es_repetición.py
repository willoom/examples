def es_repetición(cadena):
  # Devuelve True si la cadena está repetida dos veces

  lon_cadena = len(cadena)

  if lon_cadena % 2 == 1:
    return False
  else:
    mitad1 = cadena[0:int(lon_cadena/2-1)]
    mitad2 = cadena[int(lon_cadena/2):lon_cadena-1]

    print('Comparamos cadena1'+mitad1+' con cadena2:'+mitad2+'.')
    return mitad1 == mitad2


print('Prueba de repetición positiva: abcabc.')
print(es_repetición('abcabc'))

print('Prueba de repetición negativa: abccba.')
print(es_repetición('abccba'))


