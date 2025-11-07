@echo off
REM Windows setup script for Document Security Tool

echo ================================================
echo   Document Security Tool - Windows Setup
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python 3.7 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo Python found!
python --version
echo.

REM Check if pip is available
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pip is not installed!
    echo.
    pause
    exit /b 1
)

echo Installing dependencies...
echo.

REM Install required packages
python -m pip install pikepdf msoffcrypto-tool PyPDF2

if %errorlevel% equ 0 (
    echo.
    echo ================================================
    echo   Installation Complete!
    echo ================================================
    echo.
    echo To run the application, double-click:
    echo   run_windows.bat
    echo.
    echo Or run from command prompt:
    echo   python doc_security_tool.py
    echo.
) else (
    echo.
    echo ERROR: Installation failed!
    echo Please check the error messages above.
    echo.
)

pause
