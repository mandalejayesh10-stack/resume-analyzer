from openai import OpenAI
from config import settings
import json
from typing import Dict, Any

# Lazy initialize client to avoid crashes if API key is missing
def get_client():
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set. Please set it and restart the app.")
    return OpenAI(api_key=settings.openai_api_key)

class AIAnalyzer:
    
    SYSTEM_PROMPT = """Act as a professional recruiter and resume expert.
Analyze the given resume and provide detailed, actionable feedback.

Your analysis must include:
1. Resume score (0-100) based on overall quality
2. ATS score (0-100) based on ATS compatibility
3. At least 15 specific checks covering:
   - Formatting consistency
   - Keyword density and relevance
   - Action verb usage
   - Readability and clarity
   - Experience impact and quantification
   - Repetition and redundancy
   - Section completeness (contact, summary, experience, education, skills)
   - Length appropriateness
   - Grammar and spelling
   - Bullet point effectiveness
   - Achievement quantification
   - Skills relevance
   - Professional summary quality
   - Contact information completeness
   - Overall structure and organization

4. Identify weak bullet points and provide improved versions using:
   - Strong action verbs
   - Measurable impact
   - Clear achievements

5. Provide specific, actionable suggestions for improvement

Do not generate fake experience or make assumptions.
Only use the provided resume content.
Return your response as valid JSON."""

    @staticmethod
    def analyze_resume(resume_text: str) -> Dict[str, Any]:
        """Analyze resume and return structured feedback"""
        
        prompt = f"""Analyze this resume and provide detailed feedback:

{resume_text}

Return a JSON object with this exact structure:
{{
  "score": <number 0-100>,
  "ats_score": <number 0-100>,
  "checks": [
    {{"name": "check name", "status": "pass/warning/fail", "message": "detailed feedback"}},
    ... (at least 15 checks)
  ],
  "issues": [
    "issue 1",
    "issue 2",
    ...
  ],
  "weak_bullets": [
    {{"original": "weak bullet point", "improved": "improved version with action verb and impact"}},
    ...
  ],
  "suggestions": [
    "specific suggestion 1",
    "specific suggestion 2",
    ...
  ],
  "summary": "brief overall assessment"
}}"""

        try:
            response = get_client().chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": AIAnalyzer.SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            raise Exception(f"AI analysis failed: {str(e)}")
    
    @staticmethod
    def match_job_description(resume_text: str, job_description: str) -> Dict[str, Any]:
        """Match resume against job description"""
        
        prompt = f"""Compare this resume against the job description and provide a detailed match analysis.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return a JSON object with this exact structure:
{{
  "match_score": <number 0-100>,
  "missing_keywords": [
    "keyword 1",
    "keyword 2",
    ...
  ],
  "present_keywords": [
    "keyword 1",
    "keyword 2",
    ...
  ],
  "recommendations": [
    "specific recommendation 1",
    "specific recommendation 2",
    ...
  ],
  "skill_gaps": [
    "missing skill 1",
    "missing skill 2",
    ...
  ],
  "strengths": [
    "matching strength 1",
    "matching strength 2",
    ...
  ]
}}"""

        try:
            response = get_client().chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert recruiter analyzing resume-job fit."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            raise Exception(f"Job matching failed: {str(e)}")
    
    @staticmethod
    def generate_resume(role: str, skills: str, experience: str) -> Dict[str, Any]:
        """Generate a professional resume"""
        
        prompt = f"""Generate a professional resume for the following:

ROLE: {role}
SKILLS: {skills}
EXPERIENCE: {experience}

Create a well-structured resume with:
- Professional summary
- Key skills section
- Work experience with strong bullet points
- Education section
- Proper formatting

Return a JSON object with this structure:
{{
  "summary": "professional summary paragraph",
  "skills": ["skill1", "skill2", ...],
  "experience": [
    {{
      "title": "job title",
      "company": "company name",
      "duration": "time period",
      "bullets": ["achievement 1", "achievement 2", ...]
    }}
  ],
  "education": [
    {{
      "degree": "degree name",
      "institution": "school name",
      "year": "graduation year"
    }}
  ]
}}"""

        try:
            response = get_client().chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a professional resume writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            raise Exception(f"Resume generation failed: {str(e)}")
    
    @staticmethod
    def generate_cover_letter(resume_text: str, job_description: str) -> str:
        """Generate a cover letter based on resume and job description"""
        
        prompt = f"""Generate a professional cover letter based on this resume and job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Create a compelling cover letter that:
- Highlights relevant experience
- Matches key requirements
- Shows enthusiasm
- Is concise and professional

Return a JSON object with:
{{
  "cover_letter": "the complete cover letter text"
}}"""

        try:
            response = get_client().chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a professional cover letter writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            return result.get("cover_letter", "")
            
        except Exception as e:
            raise Exception(f"Cover letter generation failed: {str(e)}")
