@echo off
REM Resume Analyzer - Production Deployment Helper (Windows)

echo.
echo 🚀 Resume Analyzer - Deployment Helper
echo ======================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is required but not installed.
    echo Download from: https://git-scm.com/
    pause
    exit /b 1
)

echo 📋 Deployment Configuration:
echo   Backend: resume-analyzer-backend
echo   Frontend: resume-analyzer-app
echo   Region: Ohio (Render)
echo.

REM Check git status
git status
echo.

if not "%errorlevel%"=="0" (
    echo ❌ Not a git repository or git not working
    exit /b 1
)

echo ✅ Configuration verified
echo.

echo 📤 Deployment Instructions:
echo.
echo Step 1: Set up GitHub Secrets
echo   Go to: https://github.com/yourusername/resume-analyzer/settings/secrets/actions
echo   Add these secrets:
echo   - RENDER_API_KEY (from https://dashboard.render.com/account/api-tokens^)
echo   - RENDER_SERVICE_ID (backend service ID from Render dashboard^)
echo   - VERCEL_TOKEN (from https://vercel.com/account/tokens^)
echo   - VERCEL_ORG_ID (your Vercel organization ID^)
echo   - VERCEL_PROJECT_ID (your Vercel project ID^)
echo.

echo Step 2: Push your code
echo   git add .
echo   git commit -m "deployment: setup ci/cd"
echo   git push
echo.

echo Step 3: Monitor deployment
echo   Go to: https://github.com/yourusername/resume-analyzer/actions
echo   Watch the workflow run
echo.

echo ✅ All set!
echo.
pause
