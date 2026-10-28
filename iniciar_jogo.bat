@echo off
title Banco Imobiliario Python

mode con: cols=140 lines=40

:inicio
cls

py main.py

echo.
echo ==========================
echo 1 - Jogar novamente
echo 2 - Fechar
echo ==========================

choice /c 12 /n /m "Escolha: "

if errorlevel 2 exit
if errorlevel 1 goto inicio