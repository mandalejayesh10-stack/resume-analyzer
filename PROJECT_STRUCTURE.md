# Project Structure

Complete overview of the AI Resume Analyzer codebase.

```
resume-analyzer/
├── backend/                      # FastAPI Backend
│   ├── main.py                  # Main application & API routes
│   ├── ai_analyzer.py           # OpenAI integration & analysis logic
│   ├── file_parser.py           # PDF & DOCX parsing
│   ├── database.py              # SQLAlchemy models & database setup
│   ├── config.py                # Configuration & settings
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example            # Environment variables template
│   ├── uploads/                # Temporary file storage (gitignored)
│   └── README.md               # Backend documentation
│
├── frontend/                    # Next.js Frontend
│   ├── app/                    # Next.js App Router
│   │   ├── page.tsx           # Home page (landing)
│   │   ├── layout.tsx         # Root layout with navbar
│   │   ├── globals.css        # Global styles & Tailwind
│   │   ├── analyzer/
│   │   │   └── page.tsx       # Resume analyzer page
│   │   ├── job-match/
│   │   │   └── page.tsx       # Job matching page
│   │   ├── ai-writer/
│   │   │   └── page.tsx       # AI writer page
│   │   └── dashboard/
│   │       └── page.tsx       # Dashboard page
│   │
│   ├── components/             # React components
│   │   ├── FileUpload.tsx     # File upload component
│   │   └── Navbar.tsx         # Navigation bar
│   │
│   ├── package.json           # Node dependencies
│   ├── tsconfig.json          # TypeScript configuration
│   ├── tailwind.config.ts     # Tailwind CSS configuration
│   ├── postcss.config.js      # PostCSS configuration
│   ├── next.config.js         # Next.js configuration
│   ├── .env.local.example     # Environment variables template
│   └── README.md              # Frontend documentation
│
├── README.md                   # Main project documentation
├── QUICKSTART.md              # Quick start guide
├── DEPLOYMENT.md              # Deployment instructions
├── PROJECT_STRUCTURE.md       # This file
└── .gitignore                 # Git ignore rules
```

## Backend Architecture

### main.py
- FastAPI application setup
- CORS middleware configuration
- API route definitions
- File upload handling
- Database session management
- Error handling

**Key Routes:**
- `POST /upload` - Upload and parse resume
- `POST /analyze` - Analyze resume content
- `POST /job-match` - Match resume to job description
- `POST /generate/resume` - Generate resume
- `POST /generate/cover-letter` - Generate cover letter
- `GET /resumes` - List all resumes
- `GET /resumes/{id}` - Get specific resume

### ai_analyzer.py
- OpenAI API integration
- Structured JSON response handling
- Resume analysis logic (15+ checks)
- Job matching algorithm
- Resume generation
- Cover letter generation

**Key Methods:**
- `analyze_resume()` - Comprehensive resume analysis
- `match_job_description()` - Job matching
- `generate_resume()` - Resume generation
- `generate_cover_letter()` - Cover letter generation

### file_parser.py
- PDF parsing with pdfplumber
- DOCX parsing with python-docx
- Text extraction and cleaning
- File type validation

**Key Methods:**
- `extract_text_from_pdf()` - PDF text extraction
- `extract_text_from_docx()` - DOCX text extraction
- `clean_text()` - Text normalization
- `parse_file()` - Universal file parser

### database.py
- SQLAlchemy ORM models
- Database connection setup
- Session management
- Table definitions

**Models:**
- `Resume` - Stores resume data and analysis
- `JobMatch` - Stores job matching results

### config.py
- Environment variable loading
- Settings management
- Configuration validation

## Frontend Architecture

### Pages

#### app/page.tsx (Home)
- Landing page
- Hero section
- File upload CTA
- Features showcase
- How it works section

#### app/analyzer/page.tsx
- Resume upload interface
- Real-time analysis display
- Score visualization
- Detailed checks list
- Bullet point improvements
- Suggestions panel

#### app/job-match/page.tsx
- Resume upload
- Job description input
- Match score display
- Keyword comparison
- Recommendations

#### app/ai-writer/page.tsx
- Tabbed interface (Resume/Cover Letter)
- Input forms
- Generated content display
- Formatted output

#### app/dashboard/page.tsx
- Resume upload
- Analysis history
- Resume list with scores
- Quick navigation

### Components

#### FileUpload.tsx
- Drag & drop interface
- File type validation
- Upload progress
- Error handling
- API integration

#### Navbar.tsx
- Navigation links
- Responsive design
- Brand identity

### Styling

#### globals.css
- Tailwind directives
- Custom component classes
- Utility classes

**Custom Classes:**
- `.btn-primary` - Primary button style
- `.btn-secondary` - Secondary button style
- `.card` - Card container
- `.input` - Input field
- `.textarea` - Textarea field

## Data Flow

### Resume Analysis Flow
```
1. User uploads file (Frontend)
   ↓
2. FileUpload component sends to /upload (Backend)
   ↓
3. file_parser.py extracts text
   ↓
4. Text saved to database
   ↓
5. Frontend receives resume ID and text
   ↓
6. Frontend sends text to /analyze
   ↓
7. ai_analyzer.py processes with OpenAI
   ↓
8. Structured JSON returned
   ↓
9. Frontend displays results
```

### Job Matching Flow
```
1. User uploads resume and pastes job description
   ↓
2. Frontend sends both to /job-match
   ↓
3. ai_analyzer.py compares content
   ↓
4. Match score and keywords calculated
   ↓
5. Results displayed with recommendations
```

### AI Generation Flow
```
1. User provides inputs (role, skills, etc.)
   ↓
2. Frontend sends to /generate/resume or /generate/cover-letter
   ↓
3. ai_analyzer.py generates content with OpenAI
   ↓
4. Structured content returned
   ↓
5. Frontend formats and displays
```

## Key Technologies

### Backend
- **FastAPI**: Modern Python web framework
- **OpenAI API**: GPT-4 for analysis and generation
- **SQLAlchemy**: ORM for database operations
- **pdfplumber**: PDF text extraction
- **python-docx**: DOCX text extraction
- **Pydantic**: Data validation

### Frontend
- **Next.js 14**: React framework with App Router
- **React 18**: UI library
- **TypeScript**: Type safety
- **Tailwind CSS**: Utility-first styling
- **Axios**: HTTP client
- **React Dropzone**: File upload
- **Lucide React**: Icon library

## Environment Variables

### Backend (.env)
```
OPENAI_API_KEY=sk-...           # Required
DATABASE_URL=postgresql://...   # Required
REDIS_URL=redis://...           # Optional
CORS_ORIGINS=http://...         # Required
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://...  # Required
```

## Database Schema

### resumes
- `id` (SERIAL PRIMARY KEY)
- `filename` (VARCHAR)
- `content` (TEXT)
- `score` (FLOAT)
- `ats_score` (FLOAT)
- `analysis` (TEXT)
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

### job_matches
- `id` (SERIAL PRIMARY KEY)
- `resume_id` (INTEGER)
- `job_description` (TEXT)
- `match_score` (FLOAT)
- `missing_keywords` (TEXT)
- `recommendations` (TEXT)
- `created_at` (TIMESTAMP)

## API Response Formats

### Analyze Response
```json
{
  "score": 85,
  "ats_score": 78,
  "checks": [
    {
      "name": "Formatting",
      "status": "pass",
      "message": "Consistent formatting throughout"
    }
  ],
  "issues": ["Issue 1", "Issue 2"],
  "weak_bullets": [
    {
      "original": "Worked on projects",
      "improved": "Led 5 cross-functional projects..."
    }
  ],
  "suggestions": ["Suggestion 1", "Suggestion 2"],
  "summary": "Overall assessment"
}
```

### Job Match Response
```json
{
  "match_score": 75,
  "missing_keywords": ["Python", "AWS"],
  "present_keywords": ["React", "Node.js"],
  "recommendations": ["Add Python experience"],
  "skill_gaps": ["Cloud computing"],
  "strengths": ["Strong frontend skills"]
}
```

## Customization Points

### Modify AI Prompts
Edit `backend/ai_analyzer.py`:
- `SYSTEM_PROMPT` - Overall AI behavior
- Individual method prompts for specific features

### Customize UI
Edit frontend files:
- `tailwind.config.ts` - Colors and theme
- `app/globals.css` - Custom styles
- Component files - Layout and structure

### Add Features
1. Add backend route in `main.py`
2. Add AI logic in `ai_analyzer.py`
3. Create frontend page in `app/`
4. Add navigation in `Navbar.tsx`

## Performance Considerations

- File uploads cleaned up after processing
- Database queries optimized with indexes
- Frontend uses React Suspense for loading states
- API responses use structured JSON for fast parsing
- Images and assets optimized
- Code splitting in Next.js

## Security Features

- File type validation
- Input sanitization
- CORS protection
- Environment variable configuration
- Secure file handling
- Error messages don't leak sensitive info

---

This structure provides a clean, maintainable, and scalable foundation for the AI Resume Analyzer.
