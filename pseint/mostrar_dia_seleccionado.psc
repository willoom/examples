// Fecha: 23 de septiembre de 2025

// Autor: Willoom

// Descripci�n:
// Escribe un programa que pide un d�a de la semana y lo muestra por pantalla.
// A continuaci�n volver� a solicitarel d�a y mostrarlo hasta que el usuario seleccione el d�a cero.
// Cuando el usuario seleccione el d�a cero se acabar� el programa, sin mensajes adicionales.

Algoritmo mostrar_dia_seleccionado
	// Pedir al usuario el d�a de la semana
	Escribir "Introduzca el dia de la semana [1-7]:"
	Leer dia
	// definimos la traducci�n de n�mero de 1 a 6 y en otro caso devolvemos domingo
	Seg�n dia Hacer
		1:
			Escribir "Lunes"
		2:
			Escribir "Martes"
		3:
			Escribir "Mi�rcoles"
		4:
			Escribir "Jueves"
		5:
			Escribir "Viernes"
		6:
			Escribir "S�bado"
		7:
			Escribir "Domingo"
		De otro modo:
			Escribir "Lo siento, la semana s�lo tiene siete dias."
	FinSeg�n
FinAlgoritmo
