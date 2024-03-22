# Este programa solicitará un lado de un cuadrado
lado = float(input('Introduzca la longitud en cm del lado del cuadrado: '))

# calculará el perímetro
perímetro = 4*lado

# calculará el área
área = lado ** 2

# Imprimirá por pantalla ambos.
print('El perímetro de un cuadrado de lado {0:.2f} es {1:.2f}cm, y su área {2:.2f}cm²'.format(lado, perímetro, área))
