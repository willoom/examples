#!/bin/bash

# AUTOR: Willoom
# FECHA: 11 de diciembre de 2024
# DESCRIPCIÓN: 
#		Solicita dos apellidos y un nombre.
# 		Los imprime ordenadamente por pantalla.

# Solicitar dos apellidos y un nombre.
read -p  "Por favor, introduzca los dos apellidos y el nombre: " apellido1 apellido2 nombre

# Mostraremos Hola NOMBRE APELLIDO1 APELLIDO2.
echo "Hola $nombre $apellido1 $apellido2."

