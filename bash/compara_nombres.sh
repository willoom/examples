#!/bin/bash

read -p "Introduce un nombre: " nombre

if test "$nombre" == "Juan"
then
  echo "¡Hola Juanito!"
elif test "$nombre" == "Pedro"
then
  echo "¡Qué bueno Pedrito!"
elif test "$nombre" == "Mariano"
then
  echo "¡Cuánto tiempo, Marianín!" 
else
  echo "No te conozco."
fi
