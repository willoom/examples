/*
	AUTOR: Francisco Yuste García
	FECHA: 26 de enero de 2026
	DESCRIPCIÓN: Programa sencillo que recorre los elementos de un array de caracteres y va mostrando su posición.
*/

#include<stdio.h>

int main() {
	
	// Defino un array de caracteres
	char * cad = "Cadena random"; // Dejo que el compilador establezca el número de caracteres necesarios en memoria
	for (int i=0; i<13; i++) {
		// Itero sobre cada caracter de la cadena
		printf("En la posición %d tenemos el carácter %c.\n", i, cad[i]);
	}
	return 0;
}
