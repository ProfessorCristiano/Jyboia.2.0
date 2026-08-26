@echo off
rem ====================================================
rem            Iniciando Jyboia IDE 2.0
rem ====================================================

set "PYTHON_EXE="

:: 1. Tenta encontrar no Thonny
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Thonny\python.exe" (
    set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Thonny\python.exe"
    goto RUN
)

:: 2. Tenta encontrar na instalação do Python por usuário (AppData)
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe" (
    set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe"
    goto RUN
)
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe" (
    set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe"
    goto RUN
)
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\python.exe" (
    set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\python.exe"
    goto RUN
)
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python314\python.exe" (
    set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python314\python.exe"
    goto RUN
)

:: 3. Tenta encontrar na instalação global do Python (C:\PythonXX ou C:\Program Files)
if exist "C:\Python312\python.exe" (
    set "PYTHON_EXE=C:\Python312\python.exe"
    goto RUN
)

if exist "C:\Python313\python.exe" (
    set "PYTHON_EXE=C:\Python313\python.exe"
    goto RUN
)

if exist "C:\Python314\python.exe" (
    set "PYTHON_EXE=C:\Python314\python.exe"
    goto RUN
)

if exist "C:\Program Files\Python312\python.exe" (
    set "PYTHON_EXE=C:\Program Files\Python312\python.exe"
    goto RUN
)

if exist "C:\Program Files\Python313\python.exe" (
    set "PYTHON_EXE=C:\Program Files\Python313\python.exe"
    goto RUN
)

if exist "C:\Program Files\Python314\python.exe" (
    set "PYTHON_EXE=C:\Program Files\Python314\python.exe"
    goto RUN
)

:RUN
:: Executa com o caminho encontrado ou apela para o PATH global do sistema
if defined PYTHON_EXE (
    "%PYTHON_EXE%" "%~dp0iniciar_jyboia.py" %*
) else (
    python "%~dp0iniciar_jyboia.py" %*
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Ocorreu um erro ao iniciar o Jyboia IDE.
    pause
)
