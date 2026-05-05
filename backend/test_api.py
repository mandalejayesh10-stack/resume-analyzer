"""
Simple test script to verify API endpoints
Run: python test_api.py
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_root():
    """Test root endpoint"""
    print("\n1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200

def test_analyze():
    """Test resume analysis"""
    print("\n2. Testing resume analysis...")
    
    sample_resume = """
    John Doe
    Software Engineer
    john.doe@email.com | (555) 123-4567
    
    EXPERIENCE
    Senior Software Engineer | Tech Corp | 2020-Present
    - Developed web applications using React and Node.js
    - Worked on various projects
    - Helped team members
    
    EDUCATION
    Bachelor of Science in Computer Science
    University of Technology | 2016-2020
    
    SKILLS
    JavaScript, React, Node.js, Python, SQL
    """
    
    response = requests.post(
        f"{BASE_URL}/analyze",
        json={"resume_text": sample_resume}
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Resume Score: {data.get('score')}")
        print(f"ATS Score: {data.get('ats_score')}")
        print(f"Number of checks: {len(data.get('checks', []))}")
        print(f"Number of suggestions: {len(data.get('suggestions', []))}")
    else:
        print(f"Error: {response.text}")

def test_job_match():
    """Test job matching"""
    print("\n3. Testing job matching...")
    
    sample_resume = """
    John Doe - Software Engineer
    Skills: JavaScript, React, Node.js, Python
    Experience: 3 years in web development
    """
    
    sample_job = """
    Senior Full Stack Developer
    Required Skills: React, Node.js, TypeScript, AWS, Docker
    Experience: 3+ years
    """
    
    response = requests.post(
        f"{BASE_URL}/job-match",
        json={
            "resume_text": sample_resume,
            "job_description": sample_job
        }
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Match Score: {data.get('match_score')}%")
        print(f"Missing Keywords: {data.get('missing_keywords')}")
        print(f"Present Keywords: {data.get('present_keywords')}")
    else:
        print(f"Error: {response.text}")

def test_generate_resume():
    """Test resume generation"""
    print("\n4. Testing resume generation...")
    
    response = requests.post(
        f"{BASE_URL}/generate/resume",
        json={
            "role": "Software Engineer",
            "skills": "Python, Django, React, PostgreSQL",
            "experience": "3 years building web applications"
        }
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Generated Summary: {data.get('summary', '')[:100]}...")
        print(f"Number of skills: {len(data.get('skills', []))}")
    else:
        print(f"Error: {response.text}")

def main():
    print("=" * 50)
    print("AI Resume Analyzer - API Tests")
    print("=" * 50)
    
    try:
        test_root()
        
        # Uncomment these tests when you have OpenAI API key configured
        # test_analyze()
        # test_job_match()
        # test_generate_resume()
        
        print("\n" + "=" * 50)
        print("✓ Basic tests passed!")
        print("=" * 50)
        print("\nNote: Uncomment AI tests in test_api.py after configuring OpenAI API key")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to API")
        print("Make sure the backend is running on http://localhost:8000")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
