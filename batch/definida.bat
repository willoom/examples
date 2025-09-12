@echo off

REM Este script define la variable a. 
REM Comprueba si las variables a y b están definidas.

REM Fecha: 12 de septiembre de 2024 
REM - Willoom

set a=1
if DEFINED a ( echo Variable a definida ) else ( echo Variable a no definida )

if DEFINED b ( echo Variable b definida ) else ( echo Variable b no definida )
