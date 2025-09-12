@echo off

echo Nombre: %3
echo Apellidos: %1 %2

echo full ruta a archivo: %~f0%
echo letra de unidad: %~d0%
echo path sin unidad: %~p0%
echo nombre sin extensión: %~n0%
echo extensión: %~x0%
echo todo: %~0%