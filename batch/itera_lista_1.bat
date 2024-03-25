@echo off

REM Este script asigna una lista de valores a la variable lista
REM e itera sobre ella para mostrarlos por pantalla.

REM Fecha: 25 de marzo de 2024 
REM - Willoom

set "lista=1 2 3 4"
for %%i in (%lista%) do echo %%i
