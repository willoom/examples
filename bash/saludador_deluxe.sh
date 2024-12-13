#!/bin/bash

# AUTOR: Willoom
# FECHA: 11 de diciembre de 2024
# DESCRIPCIÓN: 
#		Solicita un nombre y dos apellidos.
# 		Los imprime ordenadamente por pantalla.

# Solicitar primer apellido.
read -p  "Por favor, introduzca el primer apellido: " apellido1

# Solicitar segundo apellido.
read -p "Por favor, introduzca el segundo apellido: " apellido2

# Solicitar el nombre.
read -p "Por favor, introduzca el nombre: " nombre

# Mostraremos Hola NOMBRE APELLIDO1 APELLIDO2.
echo "Hola $nombre $apellido1 $apellido2."

