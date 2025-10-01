#!/bin/bash

read -p "Introduce un nombre: " nombre

if test "$nombre" == "Juan"
then
  echo "¡Hola Juanito!"
elif test "$nombre" == "Pedro"
then
  echo "¡Hola Pedrito!"
else
  echo "No te conozco."
fi
