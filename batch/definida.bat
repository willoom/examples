@echo off
set a=1
if DEFINED a ( echo Variable a definida ) else ( echo Variable a no definida )
if DEFINED b ( echo Variable b definida ) else ( echo Variable b no definida )