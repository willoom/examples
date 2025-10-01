#!/bin/bash

# Fecha : 1 de octubre de 2025
# Autor : Francisco Yuste García
# Descripción : Ejemplo de valores de variable cadena.

read -p "Introduce un nombre: " nombre

case $nombre" in
  "Juan")
    echo "¡Hola Juanito!"
    ;;
  "Pedro")
    echo "¡Qué bueno, Pedrito!"
    ;;
  "Mariano")
    echo "¡Cuánto tiempo, Marianín!"
    ;;
  *)
    echo "No te conozco.";
esac
