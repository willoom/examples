@echo off

REM Este script recibe un parámetro. 
REM Si éste parámetro es la cadena vacía saltamos a ERROR y se muestra "..." por pantalla,
REM el script luego ejecuta la sección etiquetada como FIN y el script finaliza.
REM Si el parámetro no es la cadena vacía la ejecución salta directamente a la sección FIN,
REM no se imprime "..." y el script finaliza.

REM Fecha: 12 de septiembre de 2024 
REM - Willoom

if "%1"=="" goto ERROR
echo ...
goto FIN

:ERROR
echo Falta el primer par metro

:FIN
exit /b

