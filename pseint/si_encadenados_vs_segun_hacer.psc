// Fecha: 23 de septiembre de 2025
// Autor: Willoom 
// Descripción:
// 		Razonamos el uso de según frente a varios si encadenados.

Algoritmo si_encadenados_vs_segun_hacer
	edad_jordi <- 6
	
	// Para hacer esto...
	Si edad_jordi=5 Entonces
		Escribir 'Debe ir de la mano por la calle'
	FinSi
	Si edad_jordi=6 Entonces
		Escribir 'Tiene que saber vestirse solo'
	FinSi
	Si edad_jordi=7 Entonces
		Escribir 'Debe ayudar a poner la mesa'
	FinSi
	
	// ... la estructura segun- hacer es la más adecuada en caso de que esté 
	// disponible en el lenguaje de programación.
	Según edad_jordi Hacer
		5:
			Escribir 'Debe ir de la mano por la calle'
		6:
			Escribir 'Tiene que saber vestirse solo'
		7:
			Escribir 'Debe ayudar a poner la mesa'
	FinSegún
FinAlgoritmo

