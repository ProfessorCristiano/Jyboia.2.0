@echo off
rem ====================================================
rem            Iniciando Jyboia IDE 2.0
rem ====================================================

set PYTHON_EXE=C:\Users\cristiano_001325\AppData\Local\Programs\Thonny\python.exe

if exist "%PYTHON_EXE%" (
    "%PYTHON_EXE%" "%~dp0iniciar_jyboia.py" %*
) else (
    python "%~dp0iniciar_jyboia.py" %*
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Ocorreu um erro ao iniciar o Jyboia IDE.
    pause
)
