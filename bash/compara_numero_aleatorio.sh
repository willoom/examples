#!/bin/bash

# AUTOR: Willoom
# FECHA: 13 de diciembre de 2024
# DESCRIPCIÓN: 
#		Este programa generará un número aleatorio entre uno y cien.
#		Mostrará por pantalla qué número se ha generado.
#		Si el número es inferior a 30 se dirá que es menor que 30.
#		Si el número es mayor de 80 se indicará.
#		En otro caso se indicará que el número aleatorio está entre 30
#		 y 80, incluidos.

# Generamos un valor aleatorio entre 1 y 100 con la variable $RANDOM
# RANDOM%100 nos da un número entre cero y noventa y nueve.
# Si le sumamos uno obtendremos el rango que queremos: de 1 a 100.
aleatorio=$((RANDOM%100 + 1)) 

if [ $aleatorio -lt 30 ]; then
	# En este punto sabemos que el nº aleatorio es inferior a 30.
	echo "$aleatorio es inferior a 30"
elif [ $aleatorio -gt 80 ]; then
	# En este punto sabemos que el nº aleatorio es mayor a 80.
	echo "$aleatorio es superior a 80"
else
	# En este punto sabemos que el nº aleatorio no es inferior a 30
	# y tampoco es superior a 80.
	echo "$aleatorio es un valor entre 30 y 80"
fi 


