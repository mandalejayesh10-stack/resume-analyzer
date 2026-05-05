from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
import os
import shutil
from datetime import datetime
import json

from config import settings
from database import init_db, get_db, Resume, JobMatch
from file_parser import FileParser
from ai_analyzer import AIAnalyzer

app = FastAPI(title="AI Resume Analyzer API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize database
@app.on_event("startup")
def startup_event():
    init_db()

# Pydantic models
class AnalyzeRequest(BaseModel):
    resume_text: str

class JobMatchRequest(BaseModel):
    resume_text: str
    job_description: str

class GenerateResumeRequest(BaseModel):
    role: str
    skills: str
    experience: str

class GenerateCoverLetterRequest(BaseModel):
    resume_text: str
    job_description: str

class ResumeResponse(BaseModel):
    id: int
    filename: str
    content: str
    score: Optional[float]
    ats_score: Optional[float]
    analysis: Optional[str]
    created_at: datetime

# Routes
@app.get("/")
def read_root():
    return {"message": "AI Resume Analyzer API", "status": "running"}

@app.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload and parse resume file"""
    
    # Validate file type
    if not file.filename.lower().endswith(('.pdf', '.docx')):
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Please upload PDF or DOCX files."
        )
    
    # Save file temporarily
    file_path = os.path.join(UPLOAD_DIR, f"{datetime.now().timestamp()}_{file.filename}")
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Parse file
        resume_text = FileParser.parse_file(file_path, file.filename)
        
        if not resume_text or len(resume_text) < 50:
            raise HTTPException(
                status_code=400,
                detail="Could not extract sufficient text from the file. Please check the file content."
            )
        
        # Save to database
        resume = Resume(
            filename=file.filename,
            content=resume_text
        )
        db.add(resume)
        db.commit()
        db.refresh(resume)
        
        return {
            "id": resume.id,
            "filename": resume.filename,
            "content": resume_text,
            "message": "Resume uploaded and parsed successfully"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)

@app.post("/analyze")
async def analyze_resume(
    request: AnalyzeRequest,
    db: Session = Depends(get_db)
):
    """Analyze resume content using AI"""
    
    if not request.resume_text or len(request.resume_text) < 50:
        raise HTTPException(
            status_code=400,
            detail="Resume text is too short or empty"
        )
    
    try:
        # Perform AI analysis
        analysis_result = AIAnalyzer.analyze_resume(request.resume_text)
        
        return {
            "score": analysis_result.get("score", 0),
            "ats_score": analysis_result.get("ats_score", 0),
            "checks": analysis_result.get("checks", []),
            "issues": analysis_result.get("issues", []),
            "weak_bullets": analysis_result.get("weak_bullets", []),
            "suggestions": analysis_result.get("suggestions", []),
            "summary": analysis_result.get("summary", "")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/job-match")
async def match_job(
    request: JobMatchRequest,
    db: Session = Depends(get_db)
):
    """Match resume against job description"""
    
    if not request.resume_text or not request.job_description:
        raise HTTPException(
            status_code=400,
            detail="Both resume text and job description are required"
        )
    
    try:
        # Perform job matching
        match_result = AIAnalyzer.match_job_description(
            request.resume_text,
            request.job_description
        )
        
        return {
            "match_score": match_result.get("match_score", 0),
            "missing_keywords": match_result.get("missing_keywords", []),
            "present_keywords": match_result.get("present_keywords", []),
            "recommendations": match_result.get("recommendations", []),
            "skill_gaps": match_result.get("skill_gaps", []),
            "strengths": match_result.get("strengths", [])
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate/resume")
async def generate_resume(request: GenerateResumeRequest):
    """Generate a resume based on role, skills, and experience"""
    
    if not request.role or not request.skills:
        raise HTTPException(
            status_code=400,
            detail="Role and skills are required"
        )
    
    try:
        result = AIAnalyzer.generate_resume(
            request.role,
            request.skills,
            request.experience
        )
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate/cover-letter")
async def generate_cover_letter(request: GenerateCoverLetterRequest):
    """Generate a cover letter based on resume and job description"""
    
    if not request.resume_text or not request.job_description:
        raise HTTPException(
            status_code=400,
            detail="Both resume text and job description are required"
        )
    
    try:
        cover_letter = AIAnalyzer.generate_cover_letter(
            request.resume_text,
            request.job_description
        )
        
        return {"cover_letter": cover_letter}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/resumes")
async def get_resumes(db: Session = Depends(get_db)):
    """Get all uploaded resumes"""
    resumes = db.query(Resume).order_by(Resume.created_at.desc()).all()
    return resumes

@app.get("/resumes/{resume_id}")
async def get_resume(resume_id: int, db: Session = Depends(get_db)):
    """Get a specific resume by ID"""
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
