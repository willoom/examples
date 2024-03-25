@echo off

REM Este script asigna una lista de palabras a la variable lista
REM e itera sobre ella para mostrarlos por pantalla.

REM En esta variante la lista, además de no llevar comillas,
REM la declaramos con palabras en lugar de números.

REM Fecha: 25 de marzo de 2024 
REM - Willoom

REM Establecemos la página de códigos para dar soporte a los 
REM caracteres especiales de nuetro idioma con CHCP.
chcp 65001

REM Establacemos el valor de la variable lista.
set lista=En un lugar de la Mancha ...

REM Finalemnte iteramos sobre la lista, mostrando por pantalla
REM un elemento cada vez.
for %%i in (%lista%) do echo %%i