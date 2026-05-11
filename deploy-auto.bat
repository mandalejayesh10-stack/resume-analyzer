@echo off
REM Resume Analyzer - Automated Deployment Script for Windows

setlocal enabledelayedexpansion

cls
echo.
echo 🚀 Resume Analyzer - Automated Deployment
echo ==========================================
echo.

REM Step 1: Check Prerequisites
echo 📋 Step 1: Checking Prerequisites...
echo.

where python >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not installed
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✅ Python found

where node >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is required but not installed
    echo Download from: https://nodejs.org/
    pause
    exit /b 1
)
echo ✅ Node.js found

where git >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is required but not installed
    echo Download from: https://git-scm.com/
    pause
    exit /b 1
)
echo ✅ Git found

echo.

REM Step 2: Setup Backend
echo 📋 Step 2: Setting Up Backend...
echo.

cd backend

if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install -q -r requirements.txt

if not exist ".env" (
    echo Creating backend .env file...
    (
        echo OPENAI_API_KEY=
        echo DATABASE_URL=sqlite:///./resume_analyzer.db
        echo CORS_ORIGINS=*
    ) > .env
)

echo ✅ Backend setup complete
cd ..

echo.

REM Step 3: Setup Frontend
echo 📋 Step 3: Setting Up Frontend...
echo.

cd frontend

echo Installing Node.js dependencies...
call npm install -q

if not exist ".env.local" (
    echo Creating frontend .env.local file...
    (
        echo NEXT_PUBLIC_API_URL=http://localhost:8000
    ) > .env.local
)

echo ✅ Frontend setup complete
cd ..

echo.

REM Step 4: Verify Git Repository
echo 📋 Step 4: Verifying Git Repository...
echo.

git status >nul 2>&1
if errorlevel 1 (
    echo ❌ Not a git repository
    pause
    exit /b 1
)
echo ✅ Git repository found

REM Check for uncommitted changes
git status --porcelain >nul 2>&1
if not errorlevel 1 (
    git add . >nul 2>&1
    git commit -m "deployment: automated deployment setup" >nul 2>&1
)

echo.

REM Step 5: GitHub Secrets Setup
echo 📋 Step 5: GitHub Secrets Setup
echo.

echo Go to: https://github.com/yourusername/resume-analyzer/settings/secrets/actions
echo.

echo You need to add these secrets:
echo   RENDER_API_KEY       https://dashboard.render.com/account/api-tokens
echo   RENDER_SERVICE_ID    https://dashboard.render.com
echo   VERCEL_TOKEN         https://vercel.com/account/tokens
echo   VERCEL_ORG_ID        https://vercel.com/account/settings
echo   VERCEL_PROJECT_ID    https://vercel.com/dashboard
echo   OPENAI_API_KEY       https://platform.openai.com/api-keys (optional)
echo.

set /p confirm="Have you added all secrets? (y/n): "
if /i not "%confirm%"=="y" (
    echo Please add the secrets and run this script again
    pause
    exit /b 1
)

echo.

REM Step 6: Show Current Branch
echo 📋 Step 6: Current Git Status
echo.

git branch --show-current
echo.

set /p push_confirm="Ready to push to GitHub? (y/n): "
if /i "%push_confirm%"=="y" (
    echo Pushing to GitHub...
    git push origin main
    echo ✅ Pushed to GitHub
) else (
    echo Push cancelled
)

echo.

REM Step 7: Show Next Steps
echo 📋 Step 7: Deployment In Progress
echo.

echo ✅ Deployment setup complete!
echo.
echo 🎉 Your app will be live in 5-10 minutes!
echo.
echo Watch deployment at:
echo   https://github.com/yourusername/resume-analyzer/actions
echo.
echo Check status at:
echo   Render: https://dashboard.render.com
echo   Vercel: https://vercel.com/dashboard
echo.

pause
