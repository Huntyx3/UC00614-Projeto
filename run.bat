@echo off
chcp 65001 >nul 2>&1
 
title EcoRent - Servidor WSGI (Flask Waitress)
 
cd /d "%~dp0"
 
if exist "venv\Scripts\python.exe" (
    set "PYTHON=venv\Scripts\python.exe"
) else (
    set "PYTHON=python"
)

"%PYTHON%" -c "import waitress" >nul 2>&1
if errorlevel 1 (
    echo O Waitress não está instalado.
    echo Instala com:
    echo     "%PYTHON%" -m pip install waitress
    pause
    exit /b 1
)
 
echo A iniciar o Waitress...
echo Abre no navegador: http://localhost
echo Para parar o servidor: Ctrl+C
echo.
 
"%PYTHON%" wsgi.py
 
pause