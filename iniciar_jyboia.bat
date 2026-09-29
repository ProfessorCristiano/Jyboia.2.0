@echo off
setlocal enabledelayedexpansion
rem ====================================================
rem            Iniciando Jyboia IDE 2.0 (Windows)
rem ====================================================

set "PYTHON_EXE="

:: 1. Tenta o inicializador oficial do Windows (py -3)
where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    py -3 -c "import sys, tkinter; assert sys.version_info >= (3, 9)" >nul 2>&1
    if !ERRORLEVEL! EQU 0 (
        for /f "delims=" %%I in ('py -3 -c "import sys; print(sys.executable)" 2^>nul') do (
            if exist "%%~I" (
                set "PYTHON_EXE=%%~I"
                goto FOUND
            )
        )
    )
)

:: 2. Tenta o comando python no PATH do sistema
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python -c "import sys, tkinter; assert sys.version_info >= (3, 9)" >nul 2>&1
    if !ERRORLEVEL! EQU 0 (
        for /f "delims=" %%I in ('python -c "import sys; print(sys.executable)" 2^>nul') do (
            if exist "%%~I" (
                set "PYTHON_EXE=%%~I"
                goto FOUND
            )
        )
    )
)

:: 3. Busca nas instalacoes por usuario (AppData\Local\Programs\Python)
for %%V in (314 313 312 311 310 39) do (
    if exist "%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe" (
        "%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe" -c "import tkinter" >nul 2>&1
        if !ERRORLEVEL! EQU 0 (
            set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe"
            goto FOUND
        )
    )
)

:: 4. Busca nas instalacoes em Program Files (64-bit e 32-bit)
for %%V in (314 313 312 311 310 39) do (
    if exist "%ProgramFiles%\Python%%V\python.exe" (
        "%ProgramFiles%\Python%%V\python.exe" -c "import tkinter" >nul 2>&1
        if !ERRORLEVEL! EQU 0 (
            set "PYTHON_EXE=%ProgramFiles%\Python%%V\python.exe"
            goto FOUND
        )
    )
    if defined ProgramFiles(x86) (
        if exist "%ProgramFiles(x86)%\Python%%V\python.exe" (
            "%ProgramFiles(x86)%\Python%%V\python.exe" -c "import tkinter" >nul 2>&1
            if !ERRORLEVEL! EQU 0 (
                set "PYTHON_EXE=%ProgramFiles(x86)%\Python%%V\python.exe"
                goto FOUND
            )
        )
    )
)

:: 5. Busca na raiz C:\PythonXX
for %%V in (314 313 312 311 310 39) do (
    if exist "C:\Python%%V\python.exe" (
        "C:\Python%%V\python.exe" -c "import tkinter" >nul 2>&1
        if !ERRORLEVEL! EQU 0 (
            set "PYTHON_EXE=C:\Python%%V\python.exe"
            goto FOUND
        )
    )
)

:: 6. Busca na instalacao do Thonny (se existente)
if exist "%LOCALAPPDATA%\Programs\Thonny\python.exe" (
    "%LOCALAPPDATA%\Programs\Thonny\python.exe" -c "import tkinter" >nul 2>&1
    if !ERRORLEVEL! EQU 0 (
        set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Thonny\python.exe"
        goto FOUND
    )
)

:: 7. Busca no Registro do Windows (HKCU e HKLM)
for %%H in ("HKCU\Software\Python\PythonCore" "HKLM\Software\Python\PythonCore") do (
    for /f "tokens=*" %%K in ('reg query %%H 2^>nul') do (
        for /f "tokens=2*" %%A in ('reg query "%%K\InstallPath" /ve 2^>nul ^| findstr /i "REG_SZ"') do (
            if exist "%%B\python.exe" (
                "%%B\python.exe" -c "import sys, tkinter; assert sys.version_info >= (3, 9)" >nul 2>&1
                if !ERRORLEVEL! EQU 0 (
                    set "PYTHON_EXE=%%B\python.exe"
                    goto FOUND
                )
            )
        )
    )
)

:NOT_FOUND
echo ============================================================
echo [ERRO] Nao foi possivel localizar uma instalacao valida do Python.
echo ============================================================
echo.
echo O Jyboia IDE requer Python 3.9 ou superior com suporte a interface grafica (Tkinter).
echo.
echo Como resolver:
echo   1. Acesse: https://www.python.org/downloads/
echo   2. Baixe o instalador mais recente do Python para Windows.
echo   3. Durante a instalacao, marque OBRIGATORIAMENTE:
echo      [x] "Add python.exe to PATH"
echo      [x] "tcl/tk and IDLE"
echo.
pause
exit /b 1

:FOUND
"%PYTHON_EXE%" "%~dp0iniciar_jyboia.py" %*
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Ocorreu um erro ao executar o Jyboia IDE [Codigo: %ERRORLEVEL%].
    pause
)