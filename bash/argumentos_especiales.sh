#!/bin/bash

# AUTOR: willoom
# FECHA: 17 de noviembre de 2026
# DESCRIPCIÓN: Este script informa de: 
#       el comando que invoca el script, el número de argumentos recibido y
#       todos los argumentos agrupados en una cadena.


# Presentamos el script.
echo "Script invocado: $0."

# Informamos del número de parámetros que recibimos.
echo "Se han recibido $# argumentos".

# Se muestra los que se consiran argumentos de este script
echo "Los argumentos recibidos: $*"
