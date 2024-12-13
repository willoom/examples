#!/bin/bash

# AUTOR: Willoom
# FECHA: 11 de diciembre de 2024
# DESCRIPCIÓN: 
#		Informa del número de parámetros recibido.
# 		Recibe dos apellidos y un nombre y los imprime 
# 		ordenadamente por pantalla.

# Presentamos el script.
echo "Soy $0."

# Saludamos asumiendo que 
# - el primer apellido es el primer parámetro
# - el segundo apellido es el segundo parámetro y que
# - el nombre es el tercer parámetro.
# Mostraremos Hola NOMBRE APELLIDO1 APELLIDO2.
echo "Hola $3 $1 $2."

# Informamos del número de parámetros que recibimos.
echo "He recibido $# parámetros".
