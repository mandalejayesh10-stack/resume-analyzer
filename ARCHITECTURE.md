# System Architecture

Visual overview of the AI Resume Analyzer architecture.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         USER BROWSER                         │
│                     http://localhost:3000                    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ HTTP/REST
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    NEXT.JS FRONTEND                          │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│  │   Home     │  │  Analyzer  │  │ Job Match  │            │
│  │   Page     │  │    Page    │  │    Page    │            │
│  └────────────┘  └────────────┘  └────────────┘            │
│  ┌────────────┐  ┌────────────┐                             │
│  │ AI Writer  │  │ Dashboard  │                             │
│  │   Page     │  │    Page    │                             │
│  └────────────┘  └────────────┘                             │
│                                                               │
│  Components: FileUpload, Navbar                              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Axios HTTP Requests
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    FASTAPI BACKEND                           │
│                  http://localhost:8000                       │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              API ENDPOINTS                           │   │
│  │  POST /upload          - Upload & parse resume       │   │
│  │  POST /analyze         - AI analysis                 │   │
│  │  POST /job-match       - Job matching                │   │
│  │  POST /generate/resume - Generate resume             │   │
│  │  POST /generate/cover-letter - Generate cover letter │   │
│  │  GET  /resumes         - List resumes                │   │
│  │  GET  /resumes/{id}    - Get resume                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                   │
│  ┌────────────────────────┼────────────────────────────┐   │
│  │         CORE MODULES   │                             │   │
│  │  ┌──────────────┐  ┌──▼───────────┐  ┌──────────┐  │   │
│  │  │ File Parser  │  │ AI Analyzer  │  │ Database │  │   │
│  │  │              │  │              │  │  Models  │  │   │
│  │  │ - PDF Parse  │  │ - Analysis   │  │          │  │   │
│  │  │ - DOCX Parse │  │ - Job Match  │  │ - Resume │  │   │
│  │  │ - Clean Text │  │ - Generate   │  │ - Match  │  │   │
│  │  └──────────────┘  └──────────────┘  └──────────┘  │   │
│  └─────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼
    ┌──────────────┐ ┌──────────┐ ┌──────────────┐
    │   OpenAI     │ │PostgreSQL│ │   Redis      │
    │   GPT-4 API  │ │ Database │ │  (Optional)  │
    │              │ │          │ │              │
    │ - Analysis   │ │ - Resumes│ │ - Caching    │
    │ - Generation │ │ - Matches│ │              │
    └──────────────┘ └──────────┘ └──────────────┘
```

## Data Flow

### 1. Resume Upload & Analysis Flow

```
User uploads resume (PDF/DOCX)
        ↓
FileUpload component (Frontend)
        ↓
POST /upload (Backend)
        ↓
File Parser extracts text
        ↓
Save to PostgreSQL
        ↓
Return resume ID & text
        ↓
Frontend receives data
        ↓
POST /analyze with text
        ↓
AI Analyzer processes with OpenAI
        ↓
15+ checks performed
        ↓
Structured JSON returned
        ↓
Frontend displays results
```

### 2. Job Matching Flow

```
User uploads resume + pastes job description
        ↓
POST /job-match (Backend)
        ↓
AI Analyzer compares content
        ↓
Extract keywords from both
        ↓
Calculate match percentage
        ↓
Identify gaps and strengths
        ↓
Return structured results
        ↓
Frontend displays match score, keywords, recommendations
```

### 3. AI Generation Flow

```
User provides inputs (role, skills, experience)
        ↓
POST /generate/resume or /generate/cover-letter
        ↓
AI Analyzer creates prompt
        ↓
OpenAI generates content
        ↓
Structured JSON returned
        ↓
Frontend formats and displays
```

## Component Architecture

### Frontend Components

```
App Layout (layout.tsx)
├── Navbar
│   ├── Logo
│   └── Navigation Links
│
└── Page Content
    ├── Home Page
    │   ├── Hero Section
    │   ├── FileUpload Component
    │   ├── Features Section
    │   └── How It Works
    │
    ├── Analyzer Page
    │   ├── FileUpload (if no resume)
    │   ├── Resume Preview (left)
    │   └── Analysis Results (right)
    │       ├── Score Cards
    │       ├── Checks List
    │       ├── Bullet Improvements
    │       └── Suggestions
    │
    ├── Job Match Page
    │   ├── Resume Upload
    │   ├── Job Description Input
    │   └── Match Results
    │       ├── Match Score
    │       ├── Keywords
    │       └── Recommendations
    │
    ├── AI Writer Page
    │   ├── Tab Navigation
    │   ├── Resume Generator
    │   │   ├── Input Form
    │   │   └── Generated Resume
    │   └── Cover Letter Generator
    │       ├── Input Form
    │       └── Generated Letter
    │
    └── Dashboard Page
        ├── Upload Section
        └── Resume History List
```

### Backend Modules

```
FastAPI Application (main.py)
├── CORS Middleware
├── Database Session Management
├── File Upload Handler
└── API Routes
    ├── /upload
    ├── /analyze
    ├── /job-match
    ├── /generate/resume
    ├── /generate/cover-letter
    └── /resumes

AI Analyzer (ai_analyzer.py)
├── OpenAI Client
├── System Prompts
└── Methods
    ├── analyze_resume()
    ├── match_job_description()
    ├── generate_resume()
    └── generate_cover_letter()

File Parser (file_parser.py)
├── PDF Parser (pdfplumber)
├── DOCX Parser (python-docx)
└── Text Cleaner

Database (database.py)
├── SQLAlchemy Engine
├── Session Factory
└── Models
    ├── Resume
    └── JobMatch
```

## Technology Stack

### Frontend Stack
```
Next.js 14 (React Framework)
├── React 18 (UI Library)
├── TypeScript (Type Safety)
├── Tailwind CSS (Styling)
├── Axios (HTTP Client)
├── React Dropzone (File Upload)
└── Lucide React (Icons)
```

### Backend Stack
```
FastAPI (Web Framework)
├── Python 3.9+ (Language)
├── OpenAI API (AI Integration)
├── SQLAlchemy (ORM)
├── PostgreSQL (Database)
├── pdfplumber (PDF Parsing)
├── python-docx (DOCX Parsing)
└── Pydantic (Validation)
```

## Database Schema

```
┌─────────────────────────────────────┐
│            RESUMES                  │
├─────────────────────────────────────┤
│ id (PK)          SERIAL              │
│ filename         VARCHAR             │
│ content          TEXT                │
│ score            FLOAT               │
│ ats_score        FLOAT               │
│ analysis         TEXT                │
│ created_at       TIMESTAMP           │
│ updated_at       TIMESTAMP           │
└─────────────────────────────────────┘
                  │
                  │ 1:N
                  │
┌─────────────────▼───────────────────┐
│          JOB_MATCHES                │
├─────────────────────────────────────┤
│ id (PK)              SERIAL          │
│ resume_id (FK)       INTEGER         │
│ job_description      TEXT            │
│ match_score          FLOAT           │
│ missing_keywords     TEXT            │
│ recommendations      TEXT            │
│ created_at           TIMESTAMP       │
└─────────────────────────────────────┘
```

## API Request/Response Flow

### Example: Resume Analysis

**Request:**
```http
POST /analyze HTTP/1.1
Content-Type: application/json

{
  "resume_text": "John Doe\nSoftware Engineer\n..."
}
```

**Processing:**
1. Validate input
2. Send to OpenAI with structured prompt
3. Parse JSON response
4. Return structured data

**Response:**
```json
{
  "score": 85,
  "ats_score": 78,
  "checks": [
    {
      "name": "Formatting",
      "status": "pass",
      "message": "Consistent formatting"
    }
  ],
  "weak_bullets": [
    {
      "original": "Worked on projects",
      "improved": "Led 5 cross-functional projects..."
    }
  ],
  "suggestions": ["Add quantifiable metrics"],
  "summary": "Strong resume with room for improvement"
}
```

## Deployment Architecture

```
┌─────────────────────────────────────────────────────┐
│                    PRODUCTION                        │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────┐         ┌──────────────┐         │
│  │   Vercel     │         │    Render    │         │
│  │  (Frontend)  │◄───────►│  (Backend)   │         │
│  │              │  HTTPS  │              │         │
│  │  Next.js App │         │  FastAPI App │         │
│  └──────────────┘         └──────┬───────┘         │
│                                   │                  │
│                          ┌────────┼────────┐        │
│                          │        │        │        │
│                    ┌─────▼──┐ ┌──▼────┐ ┌─▼─────┐ │
│                    │ Neon   │ │OpenAI │ │ Redis │ │
│                    │  DB    │ │  API  │ │(Opt.) │ │
│                    └────────┘ └───────┘ └───────┘ │
│                                                      │
└─────────────────────────────────────────────────────┘
```

## Security Architecture

```
Security Layers
├── Frontend
│   ├── Input Validation
│   ├── File Type Checking
│   └── HTTPS Only
│
├── Backend
│   ├── CORS Protection
│   ├── File Validation
│   ├── Input Sanitization
│   └── Environment Variables
│
└── Database
    ├── Connection Pooling
    ├── Prepared Statements
    └── Encrypted Connections
```

## Performance Optimizations

```
Frontend
├── Code Splitting (Next.js)
├── Lazy Loading
├── Image Optimization
└── Minimal Bundle Size

Backend
├── Async/Await
├── Database Indexing
├── File Cleanup
└── Efficient Parsing

Caching (Optional)
└── Redis for API Responses
```

## Scalability Considerations

```
Horizontal Scaling
├── Frontend: Vercel Edge Network
├── Backend: Multiple Render Instances
└── Database: Connection Pooling

Vertical Scaling
├── Increase Server Resources
├── Optimize Database Queries
└── Add Redis Caching
```

---

This architecture provides a solid foundation for a production-ready AI Resume Analyzer SaaS application.
