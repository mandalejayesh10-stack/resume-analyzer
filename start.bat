@echo off
REM Quick Start - Resume Analyzer

echo.
echo 🚀 Resume Analyzer - Quick Start
echo ================================
echo.

echo Choose an option:
echo.
echo 1. Setup local development environment
echo 2. Deploy to production
echo 3. Open documentation
echo.

set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo Starting setup...
    call setup.bat
) else if "%choice%"=="2" (
    echo.
    echo Starting deployment...
    call deploy.bat
) else if "%choice%"=="3" (
    echo.
    echo Opening deployment guide...
    start DEPLOY_NOW.md
) else (
    echo Invalid choice. Please try again.
    pause
    call start.bat
)
