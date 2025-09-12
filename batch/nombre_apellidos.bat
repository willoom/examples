@echo off

REM Este script recibe como parámetros APELLIDO1 APELLIDO2 NOMBRE.
REM Asigna estos parámetros respectivamente a las variables %1, %2, %3.
REM Muestra por pantalla el significado.
REM Tratamos una variable que contiene una ruta a un fichero: %0.
REM %0 es el archivo del propio script.

REM Fecha: 12 de septiembre de 2024 
REM - Willoom

echo Nombre: %3
echo Apellidos: %1 %2

echo full ruta a archivo: %~f0%
echo letra de unidad: %~d0%
echo path sin unidad: %~p0%
echo nombre sin extensión: %~n0%
echo extensión: %~x0%

echo todo: %~0%
