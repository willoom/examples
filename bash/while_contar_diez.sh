#!/bin/bash

# AUTOR: Willoom
# 18 de diciembre de 2024

# Ejemplo while
# Contar del 1 al 10 con un while

# En esta variable se irá acumulando la suma
contador=0

# Número de iteración
vuelta=1

while [ vuelta -le 10 ]; do
  # acumulamos el valor actual de iteración
  contador=$( $contador + $vuelta )

  # incrementamos el iterador para garantizart que salimos del bucle en diez iteraciones.
  vuelta=$( $vuelta + 1 )
done

echo "La suma de los diez primeros naturales es $contador"
