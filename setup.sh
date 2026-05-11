#!/bin/bash

# Resume Analyzer - Local Development Setup & Testing

set -e

echo "🚀 Resume Analyzer - Development Setup"
echo "========================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    exit 1
fi

echo "✅ Python and Node.js found"
echo ""

# Setup Backend
echo "📦 Setting up Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate || . venv/Scripts/activate
pip install -r requirements.txt
echo "✅ Backend dependencies installed"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << EOF
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./resume_analyzer.db
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
EOF
    echo "✅ .env file created (add your OPENAI_API_KEY)"
fi

cd ..

# Setup Frontend
echo ""
echo "📦 Setting up Frontend..."
cd frontend
npm install
echo "✅ Frontend dependencies installed"

# Create .env.local if it doesn't exist
if [ ! -f .env.local ]; then
    echo "Creating .env.local file..."
    cat > .env.local << EOF
NEXT_PUBLIC_API_URL=http://localhost:8000
EOF
    echo "✅ .env.local file created"
fi

cd ..

echo ""
echo "✅ Setup Complete!"
echo ""
echo "📝 Next steps:"
echo "1. Add your OpenAI API key to: backend/.env"
echo "2. Start backend: cd backend && source venv/bin/activate && uvicorn main:app --reload"
echo "3. Start frontend: cd frontend && npm run dev"
echo "4. Visit: http://localhost:3000"
