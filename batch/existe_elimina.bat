@echo off

REM Este script comprueba si existe el fichero token.txt. 
REM Si es así lo borra. En otro caso indica que no existe.

REM Fecha: 12 de septiembre de 2024 
REM - Willoom

if exist token.txt (
	echo borrando token.txt
	del token.txt
) else (
	echo El fichero token.txt no existe
)

