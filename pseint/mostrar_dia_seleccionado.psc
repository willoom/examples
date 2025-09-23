// Fecha: 23 de septiembre de 2025

// Autor: Willoom

// Descripción:
// Escribe un programa que pide un día de la semana y lo muestra por pantalla.
// A continuación volverá a solicitarel día y mostrarlo hasta que el usuario seleccione el día cero.
// Cuando el usuario seleccione el día cero se acabará el programa, sin mensajes adicionales.

Algoritmo mostrar_dia_seleccionado
	// Pedir al usuario el día de la semana
	Escribir "Introduzca el dia de la semana [1-7]:"
	Leer dia
	// definimos la traducción de número de 1 a 6 y en otro caso devolvemos domingo
	Según dia Hacer
		1:
			Escribir "Lunes"
		2:
			Escribir "Martes"
		3:
			Escribir "Miércoles"
		4:
			Escribir "Jueves"
		5:
			Escribir "Viernes"
		6:
			Escribir "Sábado"
		7:
			Escribir "Domingo"
		De otro modo:
			Escribir "Lo siento, la semana sólo tiene siete dias."
	FinSegún
FinAlgoritmo
