// Fecha: 23 de septiembre de 2025
// Autor: Willoom
// Descripción
// Escribe un programa que transforma un entero, orden en la semana
// y muestra por pantalla el día de la semana
Algoritmo mostrar_dia_3_de_semana
	// Indicamos que queremos mostrar el tercer día de la semana
	dia <- 3
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
		De Otro Modo:
			Escribir "Domingo"
	FinSegún
FinAlgoritmo
