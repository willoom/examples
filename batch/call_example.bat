@echo off

REM Este script hace llamadas a subrutina 
REM con paso de parámetros.

REM Fecha: 12 de septiembre de 2024 
REM - Willoom

call :MAIN
goto :EOF

:SUMA
set /A res=%1 + %2
echo %res%
goto :EOF

:RESTA
set /A res=%1 - %2
echo %res%
goto :EOF

:MAIN
set /P arg=Escribe dos numeros separados por un espacio
echo %arg%

echo su suma es:
call :SUMA %arg%

echo su resta es:
call :RESTA %arg%

goto :EOF
