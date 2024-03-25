@echo off

REM Script: cuenta_opciones.bat

REM Este script recibe un nombre de fichero como primer parámetro. 
REM Informa de las líneas que tiene el fichero.
REM Informa si tiene diez o más líneas y termina el script.

REM Fecha: 25 de marzo de 2024 
REM Autor: willoom

REM establecemos la variable que contendrá el nombre del fichero.
set fichero=%1

REM Inicializo la variable numlineas a un valor absurdo.
set num_lineas="X"

REM Asumo que el fichero y su ruta existen.
REM Me creo un fichero auxiliar.txt con el número de líneas
REM no vacías del fichero.
type %fichero% | find "" /C /v > auxiliar.txt

REM Asigno el valor de num_lineas a partir del fichero auxiliar.txt
set /p num_lineas=<auxiliar.txt

REM Tan pronto tengo el número de líneas no nulas en la variable
REM num_lineas, elimino el fichero auxiliar.txt.
del auxiliar.txt

REM Muestro el  número de líneas/opciones del fichero.
echo El fichero %fichero% tiene %num_lineas% opciones.

REM En la variable mensaje saco factor común de la afirmación que va 
REM en función del número de líneas del fichero leído.
set mensaje=hacer un menú desde la opción 1 hasta la 9 para seleccionar cualquier línea
if %num_lineas% GEQ 10 (
  REM Nos quedamos cortos con las opciones 123456789
  echo NO podremos %mensaje%.
) else (
  REM Tenemos opciones suficientes para dar cobertura a todas las líneas.
  echo Podremos %mensaje%.
)
