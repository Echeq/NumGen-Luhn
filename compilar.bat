@echo off
REM ========================================
REM Script para compilar tarjeta.dll en Windows
REM ========================================

echo Compilando tarjeta.c ...

cd /d "%~dp0src"

where cl >nul 2>nul
if errorlevel 1 (
    echo ERROR: Compilador de Visual Studio no encontrado.
    echo.
    echo Necesitas abrir "x64 Native Tools Command Prompt" 
    echo desde Visual Studio en el Menu Inicio.
    echo.
    echo Tambien puedes ejecutar desde Developer Console:
    echo   cl /LD /Fe:..\tarjeta.dll tarjeta.c
    pause
    exit /b 1
)

cl /LD /Fe:..\tarjeta.dll tarjeta.c

if exist ..\tarjeta.dll (
    echo.
    echo OK: tarjeta.dll generado exitosamente.
    cd .. 
    dir tarjeta.dll
) else (
    echo.
    echo ERROR: Fallo la compilacion.
)
pause