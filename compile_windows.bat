@echo off
REM Compile Document Security Tool for Windows
REM Run this script ON A WINDOWS MACHINE to create .exe

echo ================================================
echo   Document Security Tool - Windows Compiler
echo ================================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo Installing PyInstaller...
python -m pip install pyinstaller

echo.
echo Compiling to Windows executable...
echo This may take a few minutes...
echo.

REM Compile with PyInstaller
python -m PyInstaller --onefile --windowed --name "DocumentSecurityTool" doc_security_tool.py

if %errorlevel% equ 0 (
    echo.
    echo ================================================
    echo   Compilation Successful!
    echo ================================================
    echo.
    echo Executable created at:
    echo   dist\DocumentSecurityTool.exe
    echo.
    echo You can now run DocumentSecurityTool.exe without Python!
    echo.
) else (
    echo.
    echo ERROR: Compilation failed!
    echo.
)

pause
