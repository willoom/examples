#include <stdio.h>
#include <stdlib.h>

/*
	Autor: Willoom
	Fecha: 9 de diciembre de 2024
	Descripción:

		Este programa dibuja por pantalla tres cadenas de caracteres capicua,
		con espacios y el caracter '#'.

		Para ello nos valemos de una función que recibe un radio máximo y un radio
		del capicua a representar.


		Ejemplo string_capicua(3,2) nos devolverá la cadena 
		{' ','#', '#', '#', ' ','\0'}

*/


/* 
Construimos la subcadena en función de un radio respecto de un radio máximo.
Reserva espacio en la pila y devolverá su puntero con la cadena de caracteres esperada.

	El eje de capicua ocupa la posición radio_máximo en el array.

	E.g.: Capicua de radio 1 en este ejercicio simplificado sería '  #  '
	E.g.: Capicua de radio 3 en este ejercicio simplificado sería ' ### '
	E.g.: Capicua de radio 3 en este ejercicio simplificado sería '#####'

	PARÁMETROS
	radio_max nos sirve para conocer el radio mayor de referencia,
	radio es el radio del capicua que hemos de representar con caracteres ASCII,
	
	RETORNA la representación ASCII elaborada por la función.

	OJO cuando el espacio reservado deje de ser útil, sería conveniente liberarlo con la función free().
*/

char* string_de_capicua(int radio_max, int radio) {
	

	// calculamos el tamaño de la subcadena en función del radio mayor 
	int capicua_size = radio_max * 2;
	
	/* 
		El espacio a reservar de pila será igual al tamaño en mamoria del tipo carácter 
		por el número de caracteres.
		Importante: acordarnos que una cadena de caracteres tiene un último carácter terminador ''
	*/
	char* capicua_string = (char*) malloc(sizeof(char)*capicua_size);
	

	// hallamos a partir de qué posición hemos de poner '#'
	int capicua_inicio = radio_max - radio;

	int eje_posicion = radio_max; // posición en el array del centro del eje
	// printf("diametro_max: %d, eje_posicion: %d, disco_inicio: %d\n", diametro_max, eje_posicion, disco_inicio);
	for (int i=0; i < eje_posicion; i++) {
		if (i < capicua_inicio) {
			capicua_string[i] = ' ';
			capicua_string[(capicua_size - 2) - i] = ' ';
		} else {
			capicua_string[i] = '#';
			capicua_string[(capicua_size - 2) - i] = '#';
		}
	}

	// clausuramos la string
	capicua_string[capicua_size - 1] = '\0';
	
	return capicua_string;
}

int main(int argc, char *argv[]) {

	// Declaramos las variables que usaremos para representar tres discos
	char *c1, *c2, *c3, *c4, *c5;
	
	// Generamos la representación en string de los capicuas de radio 1 2 3 4 5
	// respectivamente. En el interior se reserva espacio de pila.
	c1 = string_de_capicua(5,1);
	c2 = string_de_capicua(5,2);
	c3 = string_de_capicua(5,3);
	c4 = string_de_capicua(5,4);
	c5 = string_de_capicua(5,5);

	// Imprimimos sucesivamente los capicuas de radio 1 2 3 4 5
	printf("%s \n", c1);
	printf("%s \n", c2);
	printf("%s \n", c3);
	printf("%s \n", c4);
	printf("%s \n", c5);

	// Devolvemos el espacio reservado en pila cuando deja de ser necesario
	free(c1);
	free(c2);
	free(c3);
	free(c4);
	free(c5);

	return 0;

}
