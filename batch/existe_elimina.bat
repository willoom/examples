@echo off
if exist token.txt (
	echo borrando token.txt
	del token.txt
) else (
	echo El fichero token.txt no existe
)
