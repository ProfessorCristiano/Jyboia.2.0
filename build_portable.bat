@echo off
REM ============================================================
REM  Jybóia IDE — Script de Build do Portable Windows
REM  Gera uma distribuição 100% autônoma com Python embutido
REM ============================================================
setlocal EnableDelayedExpansion

echo.
echo  ╔══════════════════════════════════════════╗
echo  ║    Jybóia IDE — Build Portable Windows   ║
echo  ╚══════════════════════════════════════════╝
echo.

set "PYTHON_EXE="

REM --- 1. Tenta encontrar no Thonny ---
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Thonny\python.exe" (
    set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Thonny\python.exe"
    goto PYTHON_FOUND
)
if exist "%LOCALAPPDATA%\Programs\Thonny\python.exe" (
    set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Thonny\python.exe"
    goto PYTHON_FOUND
)

REM --- 2. Tenta encontrar na instalação do Python por usuário (AppData) ---
for %%v in (314 313 312 311 310 39 38) do (
    if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python%%v\python.exe" (
        set "PYTHON_EXE=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python%%v\python.exe"
        goto PYTHON_FOUND
    )
    if exist "%LOCALAPPDATA%\Programs\Python\Python%%v\python.exe" (
        set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python%%v\python.exe"
        goto PYTHON_FOUND
    )
)

REM --- 3. Tenta encontrar na raiz C:\PythonXX ---
for %%v in (314 313 312 311 310 39 38) do (
    if exist "C:\Python%%v\python.exe" (
        set "PYTHON_EXE=C:\Python%%v\python.exe"
        goto PYTHON_FOUND
    )
)

REM --- 4. Tenta encontrar em C:\Program Files\PythonXX ---
for %%v in (314 313 312 311 310 39 38) do (
    if exist "C:\Program Files\Python%%v\python.exe" (
        set "PYTHON_EXE=C:\Program Files\Python%%v\python.exe"
        goto PYTHON_FOUND
    )
    if exist "C:\Program Files (x86)\Python%%v\python.exe" (
        set "PYTHON_EXE=C:\Program Files (x86)\Python%%v\python.exe"
        goto PYTHON_FOUND
    )
)

REM --- 5. Tenta python diretamente do PATH do sistema ---
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_EXE=python"
    goto PYTHON_FOUND
)

REM --- 6. Tenta o launcher 'py' do Windows ---
py -3 --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_EXE=py -3"
    goto PYTHON_FOUND
)

:PYTHON_NOT_FOUND
echo [ERRO] Nenhuma instalacao do Python foi encontrada no computador.
echo        Locais verificados:
echo        - Thonny (AppData\Local\Programs\Thonny)
echo        - AppData do usuario (Python 3.8 ate 3.14)
echo        - C:\PythonXX e C:\Program Files\PythonXX
echo        - PATH global do sistema
echo.
echo        Por favor, instale o Python em https://www.python.org/downloads/
echo        e marque a opcao "Add Python to PATH" durante a instalacao.
echo.
pause
exit /b 1

:PYTHON_FOUND
for /f "tokens=*" %%v in ('%PYTHON_EXE% --version 2^>^&1') do set PYVER=%%v
echo [OK] Python detectado: %PYVER%
echo      Executavel: %PYTHON_EXE%
echo.

"%PYTHON_EXE%" "%~dp0build_portable.py"
if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Ocorreu uma falha durante o processo de build.
    pause
    exit /b 1
)

echo.
REM --- Perguntar se quer testar agora ---
set /p TESTAR="Deseja testar o executavel agora? (S/N): "
if /i "!TESTAR!"=="S" (
    echo Iniciando Jyboia.exe...
    start "" "dist\Jyboia\Jyboia.exe"
)

pause
endlocal
