#!/bin/bash

# Fecha: 1 de octubre de 2025
# Autor: Francisco Yuste garcía
# Descripción: Bucle while que muestra cuenta atrás de 10 a 0

# Establecemos variabla desde la que haremos cuenta atrás
contador=10

while [ $contador -gt 0 ]
do
  echo "$contador... "
  contador=$(expr $contador - 1)
  sleep 1
done

echo "0!!!!!"
