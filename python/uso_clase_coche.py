# Del módulo clase_coche importamos la clase Coche
from clase_coche import Coche

# Nos creamos cinco objetos de la clase Coche.
coche1 = Coche("Seat", 5, "Panda","CA-3553-AJ")
coche2 = Coche("Citroën", 7, "C15","B-4553-AK")
coche3 = Coche("Nissan", 5, "Almera","M-5300-AJ")
coche4 = Coche("Mitsubishi", 5, "Evo","MA-0011-QJ")
coche5 = Coche("Ferrari", 2, "Testarrossa","IT-6007-ET")

# Creamos una lista con los cinco coches creados.
coches = [coche1, coche2, coche3, coche4, coche5]

# Iteramos sobre ella y mostramos la representaciónde caracteres
# de cada uno, línea a línea.
for c in coches:
  print(c)

# Arrancamos el primer coche llamado al método correspondiente.
print("Arrancamos el coche 1...")
coche1.arrancar()

# Aceleramos el primer coche llamado al método correspondiente.
print("Aceleramos el coche 1...")
coche1.acelerar()

# Frenamos el primer coche llamado al método correspondiente.
print("Frenamos el coche 1... ")
coche1.frenar()
