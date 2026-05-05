# AI Resume Analyzer SaaS

A complete AI-powered resume analysis platform that helps job seekers optimize their resumes for ATS systems and improve their chances of landing interviews.

## Features

### 1. Resume Upload & Parsing
- Accept PDF and DOCX files
- Extract and clean resume text
- Graceful error handling

### 2. AI Resume Analysis
- **Resume Score (0-100)**: Overall quality assessment
- **ATS Score (0-100)**: ATS compatibility rating
- **15+ Comprehensive Checks**:
  - Formatting consistency
  - Keyword density
  - Action verb usage
  - Readability
  - Experience impact
  - Repetition detection
  - Section completeness
  - Length appropriateness
  - Grammar and spelling
  - Bullet point effectiveness
  - Achievement quantification
  - Skills relevance
  - Professional summary quality
  - Contact information
  - Overall structure

### 3. Suggestions Engine
- Identify weak bullet points
- Rewrite bullets with strong action verbs
- Provide measurable impact improvements
- Clear, actionable suggestions

### 4. Job Description Matching
- Compare resume against job descriptions
- Extract and match keywords
- Calculate match percentage
- Identify missing keywords
- Provide improvement recommendations

### 5. AI Resume & Cover Letter Generator
- Generate professional resumes from role, skills, and experience
- Create tailored cover letters based on job descriptions
- Rewrite and improve existing content

### 6. ATS Optimization
- Analyze ATS compatibility
- Suggest formatting fixes
- Identify missing keywords
- Recommend structure improvements

## Tech Stack

### Frontend
- **Next.js 14** (App Router)
- **React 18**
- **Tailwind CSS**
- **TypeScript**
- **Axios** for API calls
- **React Dropzone** for file uploads
- **Lucide React** for icons

### Backend
- **FastAPI** (Python)
- **OpenAI API** (GPT-4)
- **PostgreSQL** for data storage
- **SQLAlchemy** ORM
- **pdfplumber** for PDF parsing
- **python-docx** for DOCX parsing
- **Pydantic** for validation

## Installation

### Prerequisites
- Node.js 18+ and npm/yarn
- Python 3.9+
- PostgreSQL database
- OpenAI API key

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Configure environment variables in `.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/resume_analyzer
REDIS_URL=redis://localhost:6379
CORS_ORIGINS=http://localhost:3000
```

6. Initialize database:
```bash
python -c "from database import init_db; init_db()"
```

7. Run the server:
```bash
uvicorn main:app --reload
```

Backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Create `.env.local` file:
```bash
cp .env.local.example .env.local
```

4. Configure environment variables in `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

5. Run the development server:
```bash
npm run dev
# or
yarn dev
```

Frontend will be available at `http://localhost:3000`

## API Endpoints

### POST /upload
Upload and parse resume file
- **Input**: Multipart form data with file
- **Output**: Resume ID, filename, and extracted text

### POST /analyze
Analyze resume content
- **Input**: `{ "resume_text": "..." }`
- **Output**: Scores, checks, issues, suggestions, weak bullets

### POST /job-match
Match resume against job description
- **Input**: `{ "resume_text": "...", "job_description": "..." }`
- **Output**: Match score, missing keywords, recommendations

### POST /generate/resume
Generate resume from inputs
- **Input**: `{ "role": "...", "skills": "...", "experience": "..." }`
- **Output**: Structured resume with summary, skills, experience, education

### POST /generate/cover-letter
Generate cover letter
- **Input**: `{ "resume_text": "...", "job_description": "..." }`
- **Output**: Professional cover letter text

### GET /resumes
Get all uploaded resumes

### GET /resumes/{id}
Get specific resume by ID

## Usage

### 1. Upload Resume
- Go to homepage
- Drag & drop or click to upload PDF/DOCX resume
- System parses and extracts text

### 2. View Analysis
- Automatically redirected to analyzer page
- See resume score and ATS score
- Review 15+ detailed checks
- Get bullet point improvements
- Read actionable suggestions

### 3. Match Job Description
- Navigate to Job Match page
- Upload resume
- Paste job description
- Click "Analyze Match"
- View match percentage, missing keywords, and recommendations

### 4. Generate Content
- Navigate to AI Writer page
- **Resume Generator**: Enter role, skills, and experience
- **Cover Letter Generator**: Provide resume and job description
- Get professionally written content

### 5. View Dashboard
- See all uploaded resumes
- View analysis history
- Quick access to previous analyses

## Deployment

### Frontend (Vercel)

1. Push code to GitHub
2. Import project in Vercel
3. Set environment variables:
   - `NEXT_PUBLIC_API_URL`: Your backend URL
4. Deploy

### Backend (Render/Railway)

1. Push code to GitHub
2. Create new Web Service
3. Set environment variables:
   - `OPENAI_API_KEY`
   - `DATABASE_URL`
   - `CORS_ORIGINS`
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Deploy

### Database (Neon/Supabase)

1. Create PostgreSQL database
2. Copy connection string
3. Update `DATABASE_URL` in backend environment

## Key Features

✅ **No Fake Data**: All results generated from actual user input
✅ **Real-time Analysis**: Live progress indicators during processing
✅ **Structured JSON Output**: All AI responses in consistent format
✅ **15+ Quality Checks**: Comprehensive resume evaluation
✅ **ATS Optimization**: Specific recommendations for ATS systems
✅ **Job Matching**: Compare resume against job descriptions
✅ **AI Generation**: Create resumes and cover letters
✅ **Clean UI**: Professional, minimal design
✅ **Responsive**: Works on all devices
✅ **Fast**: Optimized for performance

## AI Prompt Design

The system uses carefully crafted prompts to ensure:
- Professional recruiter perspective
- Actionable, specific feedback
- No fake data or assumptions
- Structured JSON responses
- Focus on measurable improvements

## Security

- File validation (PDF/DOCX only)
- Input sanitization
- CORS protection
- Environment variable configuration
- Secure file handling

## License

MIT License - feel free to use for personal or commercial projects

## Support

For issues or questions, please open an issue on GitHub.

---

Built with ❤️ using Next.js, FastAPI, and OpenAI
