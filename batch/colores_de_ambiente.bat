@echo off

REM Script: colores_de_ambiente.bat

REM Descripción: 
REM             Pequeña librería para modificar colores en librojuego de MS-DOS.
REM             Se harán diversas llamadas a subrutinas con parámetros para probarlos.

REM Autor: willoom
REM Fecha: 10/03/2024


REM Definición de constantes de ambientes
set NOCHE=07
set DIA=3f
set VICTORIA=02
set DERROTA=04
set INTERIOR=08
set INTERACCIONA=e0

REM Establecemos  una página de códigos para que se impriman 
REM correctamente las tipografías de nuestro idioma.
CHCP 65001

REM Prueba pausada de todos los ambientes.
call :poner_ambiente %NOCHE%
echo Que se haga la noche.
pause

call :poner_ambiente %DIA%
echo Que se haga el día.
pause

call :poner_ambiente %INTERIOR%
echo Vive tu mundo interior.
pause

call :poner_ambiente %INTERACCIONA%
echo Únete al mundo.
pause

call :poner_ambiente %DERROTA%
echo Conoce la derrota.
pause

call :poner_ambiente %VICTORIA%
echo Alcanza la victoria.
pause

goto fin


REM Esta subrutina recibe un parámetro con el color de terminal a establecer.
:poner_ambiente
    cls
    color %1
    exit /b

REM Fin del script
:fin
