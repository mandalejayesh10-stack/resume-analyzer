# AI Resume Analyzer - Backend

FastAPI backend for AI-powered resume analysis.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your credentials
```

4. Initialize database:
```bash
python -c "from database import init_db; init_db()"
```

5. Run server:
```bash
uvicorn main:app --reload
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string (optional)
- `CORS_ORIGINS`: Comma-separated list of allowed origins

## Database Schema

### Resumes Table
- id: Primary key
- filename: Original filename
- content: Extracted text
- score: Resume score (0-100)
- ats_score: ATS score (0-100)
- analysis: JSON analysis results
- created_at: Timestamp
- updated_at: Timestamp

### Job Matches Table
- id: Primary key
- resume_id: Foreign key to resumes
- job_description: Job description text
- match_score: Match percentage
- missing_keywords: JSON array
- recommendations: JSON array
- created_at: Timestamp

## File Structure

- `main.py`: FastAPI application and routes
- `ai_analyzer.py`: OpenAI integration and analysis logic
- `file_parser.py`: PDF and DOCX parsing
- `database.py`: SQLAlchemy models and database setup
- `config.py`: Configuration and settings
- `requirements.txt`: Python dependencies

## Testing

```bash
# Run with test data
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"resume_text": "Your resume text here"}'
```

## Deployment

### Render
1. Connect GitHub repository
2. Set environment variables
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Railway
1. Connect GitHub repository
2. Set environment variables
3. Railway auto-detects Python and runs the app

## Performance

- Uses structured JSON output for consistent parsing
- Implements error handling for all API calls
- Validates file types before processing
- Cleans up temporary files after processing
