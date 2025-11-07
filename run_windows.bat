@echo off
REM Windows launcher for Document Security Tool

echo ================================================
echo   Document Security Tool - Windows
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Run the application
python doc_security_tool.py

pause
