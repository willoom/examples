@echo off
if "%1"=="" goto ERROR
echo ...
goto FIN

:ERROR
echo Falta el primer par metro

:FIN
exit /b
