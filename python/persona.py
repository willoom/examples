# Definimos una clase Persona
class Persona:

  # Este costructor recibe los tres atribus con los que hemos 
  # definido la clase persona y crea un objeto de la clase
  def __init__(self,nombre,dni, edad):
    self.nombre = nombre
    self.dni = dni
    self.edad = edad

  # Imprime por pantalla un mensaje inteligible para humanos
  # con los datos de la Persona
  def imprimir(self):
    print('Nombre:', self.nombre)
    print('DNI:', self.dni)
    print('Edad:', self.edad)


# A partir de aquí usaremos la clase que hemos definido.

# Creamos una lista que contendrá objetos Persona.
personas = []

# Pedimos que el usuario indique si desea agregar una nueva persona
while input('¿Desea continuar? [y/n] ')=='y':
  # Ejecutaremos este bloque mientras el usuario pulse 'y'

  # Creamos un objeto persona con la información introducida por 
  # el usuario. 
  # Se debería capturar la excepción de valor erróneo por el entero.
  p = Persona(input('Nombre:'), input('DNI:'), int(input('Edad:')))

  # Agregamos a la lista la persona
  personas.append(p)

# Aquí mostramos todas las personas
for i in personas:
  i.imprimir()

# Y ahora indicamos quién es la persona mayor de todas.
mayor = personas[0]
for i in personas:
  if mayor.edad < i.edad:
    mayor = i

print('La persona de mayor edad es: ', mayor.nombre)
