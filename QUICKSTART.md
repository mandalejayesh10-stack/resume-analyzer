# Quick Start Guide

Get the AI Resume Analyzer running in 5 minutes.

## Prerequisites

- Node.js 18+ installed
- Python 3.9+ installed
- PostgreSQL installed (or use Neon free tier)
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## 1. Clone & Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd resume-analyzer

# Or if you're already in the directory, you're good!
```

## 2. Backend Setup (Terminal 1)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env  # Windows
# or
cp .env.example .env    # Mac/Linux

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-proj-your-key-here
# DATABASE_URL=postgresql://user:password@localhost:5432/resume_analyzer

# Initialize database
python -c "from database import init_db; init_db()"

# Run the server
uvicorn main:app --reload
```

Backend will run at: http://localhost:8000

## 3. Frontend Setup (Terminal 2)

```bash
# Navigate to frontend (from project root)
cd frontend

# Install dependencies
npm install
# or
yarn install

# Create .env.local file
copy .env.local.example .env.local  # Windows
# or
cp .env.local.example .env.local    # Mac/Linux

# The default API URL is already set to http://localhost:8000
# No need to edit unless your backend runs on a different port

# Run the development server
npm run dev
# or
yarn dev
```

Frontend will run at: http://localhost:3000

## 4. Test the Application

1. Open http://localhost:3000 in your browser
2. Upload a sample resume (PDF or DOCX)
3. View the analysis results
4. Try the Job Match feature
5. Test the AI Writer

## Troubleshooting

### Backend Issues

**Error: "No module named 'pdfplumber'"**
```bash
pip install -r requirements.txt
```

**Error: "Could not connect to database"**
- Make sure PostgreSQL is running
- Check DATABASE_URL in .env
- Or use Neon (free): https://neon.tech

**Error: "Invalid OpenAI API key"**
- Check your API key in .env
- Make sure it starts with "sk-"
- Verify it's active at https://platform.openai.com

### Frontend Issues

**Error: "Cannot connect to API"**
- Make sure backend is running on port 8000
- Check NEXT_PUBLIC_API_URL in .env.local
- Verify no CORS errors in browser console

**Error: "Module not found"**
```bash
rm -rf node_modules package-lock.json
npm install
```

## Using Without PostgreSQL (Quick Test)

If you want to test without setting up PostgreSQL:

1. Edit `backend/database.py` and change:
```python
# From:
engine = create_engine(settings.database_url)

# To:
engine = create_engine("sqlite:///./test.db")
```

2. Run the backend as normal

Note: SQLite is for testing only. Use PostgreSQL for production.

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment
- Customize the UI in `frontend/app/`
- Modify AI prompts in `backend/ai_analyzer.py`

## Common Commands

### Backend
```bash
# Run server
uvicorn main:app --reload

# Run on different port
uvicorn main:app --reload --port 8001

# View API docs
# Open http://localhost:8000/docs
```

### Frontend
```bash
# Development
npm run dev

# Build for production
npm run build

# Run production build
npm start

# Lint code
npm run lint
```

## Getting Help

- Check the logs in your terminal
- Review error messages carefully
- Ensure all environment variables are set
- Verify all dependencies are installed

---

You're all set! Start analyzing resumes with AI 🚀
