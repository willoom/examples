class Coche:

  def __init__(self, marca, plazas, modelo, matrícula): 
    self.marca = marca
    self.plazas = plazas
    self.modelo = modelo
    self.matrícula = matrícula

  def __str__(self):
    descripción = "El coche con matrícula {0}, es el modelo {1} de la marca {2} y tiene {3} plazas, ".format(
                    self.matrícula,
                    self.modelo,
                    self.marca,
                    self.plazas
                  );
    return descripción

  def arrancar(self):
    print("Brum! Brum!")

  def acelerar(self):
    for i in range(3):
      print("... {0}km/h".format(50*i))

  def frenar(self):
    for i in range(3):
      print("... {0}km/h".format(50*(2-i)))

