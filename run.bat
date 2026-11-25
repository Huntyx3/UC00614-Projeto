@echo off
REM Impede que os comandos sejam mostrados no terminal.

title Servidor Flask Waitress
REM Define o titulo da janela do terminal.

cd /d "%~dp0"
REM Entra automaticamente na pasta onde esta este ficheiro .bat.

echo A iniciar o servidor...
REM Apresenta uma mensagem informativa no terminal.

set "PYTHON=venv\Scripts\python.exe"
REM Usa o Python do ambiente virtual (venv)

echo Servidor a correr. Ctrl+C para parar o servidor
"%PYTHON%" wsgi.py
REM Executa wsgi.py, que contém o proxy para comunicar com apache server