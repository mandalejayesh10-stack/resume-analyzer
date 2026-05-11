@echo off
REM Resume Analyzer - Local Development Setup & Testing (Windows)

echo.
echo 🚀 Resume Analyzer - Development Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 3 is required but not installed.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is required but not installed.
    echo Download from: https://nodejs.org/
    pause
    exit /b 1
)

echo ✅ Python and Node.js found
echo.

REM Setup Backend
echo 📦 Setting up Backend...
cd backend
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo ✅ Backend dependencies installed

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    (
        echo OPENAI_API_KEY=your_api_key_here
        echo DATABASE_URL=sqlite:///./resume_analyzer.db
        echo CORS_ORIGINS=http://localhost:3000,http://localhost:5173
    ) > .env
    echo ✅ .env file created (add your OPENAI_API_KEY^)
)

cd ..

REM Setup Frontend
echo.
echo 📦 Setting up Frontend...
cd frontend
call npm install
echo ✅ Frontend dependencies installed

REM Create .env.local if it doesn't exist
if not exist ".env.local" (
    echo Creating .env.local file...
    (
        echo NEXT_PUBLIC_API_URL=http://localhost:8000
    ) > .env.local
    echo ✅ .env.local file created
)

cd ..

echo.
echo ✅ Setup Complete!
echo.
echo 📝 Next steps:
echo 1. Add your OpenAI API key to: backend\.env
echo 2. Start backend:
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn main:app --reload
echo 3. Start frontend (new terminal):
echo    cd frontend
echo    npm run dev
echo 4. Visit: http://localhost:3000
echo.
pause
