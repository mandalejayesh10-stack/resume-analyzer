# 🎨 Visual Guide

Quick visual reference for the AI Resume Analyzer.

## 🗂️ Project Structure

```
resume-analyzer/
│
├── 📱 FRONTEND (Next.js + React + TypeScript)
│   ├── app/
│   │   ├── 🏠 page.tsx              → Landing Page
│   │   ├── 📊 analyzer/             → Resume Analyzer
│   │   ├── 🎯 job-match/            → Job Matching
│   │   ├── ✨ ai-writer/            → AI Writer
│   │   └── 📈 dashboard/            → Dashboard
│   │
│   └── components/
│       ├── 📤 FileUpload.tsx        → Upload Component
│       └── 🧭 Navbar.tsx            → Navigation
│
├── 🔧 BACKEND (FastAPI + Python)
│   ├── 🚀 main.py                   → API Routes
│   ├── 🤖 ai_analyzer.py            → AI Logic
│   ├── 📄 file_parser.py            → File Parsing
│   ├── 💾 database.py               → Database Models
│   └── ⚙️  config.py                → Configuration
│
└── 📚 DOCUMENTATION
    ├── 🎯 START_HERE.md             → Start Here!
    ├── ⚡ QUICKSTART.md             → 5-Min Setup
    ├── 📖 README.md                 → Full Docs
    ├── 🚢 DEPLOYMENT.md             → Deploy Guide
    ├── 🏗️  ARCHITECTURE.md          → System Design
    ├── ✅ FEATURES.md               → Feature List
    └── 🤝 CONTRIBUTING.md           → Contribute
```

## 🔄 User Flow

```
┌─────────────────────────────────────────────────────────┐
│                    USER JOURNEY                          │
└─────────────────────────────────────────────────────────┘

1️⃣  UPLOAD
    User visits homepage
         ↓
    Drags & drops resume (PDF/DOCX)
         ↓
    File uploaded & parsed
         ↓
    Text extracted

2️⃣  ANALYZE
    Resume sent to AI
         ↓
    GPT-4 analyzes content
         ↓
    15+ checks performed
         ↓
    Scores calculated
         ↓
    Results displayed

3️⃣  IMPROVE
    User reviews suggestions
         ↓
    Sees weak bullets
         ↓
    Gets improved versions
         ↓
    Applies changes

4️⃣  MATCH
    User pastes job description
         ↓
    AI compares content
         ↓
    Match score calculated
         ↓
    Missing keywords shown
         ↓
    Recommendations provided

5️⃣  GENERATE
    User provides inputs
         ↓
    AI generates content
         ↓
    Resume/cover letter created
         ↓
    User downloads/copies
```

## 🎨 UI Layout

### Home Page
```
┌─────────────────────────────────────────────┐
│  🧭 Navbar                                   │
├─────────────────────────────────────────────┤
│                                              │
│         🎯 AI Resume Analyzer                │
│                                              │
│    Get instant AI-powered feedback          │
│                                              │
│  ┌────────────────────────────────────┐    │
│  │                                     │    │
│  │     📤 Upload Resume Here          │    │
│  │                                     │    │
│  └────────────────────────────────────┘    │
│                                              │
│  ┌──────┐  ┌──────┐  ┌──────┐              │
│  │ 📊   │  │ 🎯   │  │ ✨   │              │
│  │Analyze│  │Match │  │Write │              │
│  └──────┘  └──────┘  └──────┘              │
│                                              │
└─────────────────────────────────────────────┘
```

### Analyzer Page
```
┌─────────────────────────────────────────────┐
│  🧭 Navbar                                   │
├─────────────────────────────────────────────┤
│                                              │
│  ┌──────────────┐  ┌──────────────────┐    │
│  │              │  │  📊 Scores        │    │
│  │   Resume     │  │  Resume: 85/100   │    │
│  │   Preview    │  │  ATS: 78/100      │    │
│  │              │  ├──────────────────┤    │
│  │   [Text]     │  │  ✅ Checks        │    │
│  │   [Text]     │  │  • Formatting ✓   │    │
│  │   [Text]     │  │  • Keywords ⚠     │    │
│  │              │  │  • Action Verbs ✓ │    │
│  │              │  ├──────────────────┤    │
│  │              │  │  💡 Suggestions   │    │
│  │              │  │  • Add metrics    │    │
│  │              │  │  • Use verbs      │    │
│  └──────────────┘  └──────────────────┘    │
│                                              │
└─────────────────────────────────────────────┘
```

### Job Match Page
```
┌─────────────────────────────────────────────┐
│  🧭 Navbar                                   │
├─────────────────────────────────────────────┤
│                                              │
│  ┌──────────────┐  ┌──────────────────┐    │
│  │   Resume     │  │  Job Description  │    │
│  │   Upload     │  │                   │    │
│  │              │  │  [Paste here]     │    │
│  └──────────────┘  └──────────────────┘    │
│                                              │
│         🎯 Analyze Match                     │
│                                              │
│  ┌─────────────────────────────────────┐   │
│  │     Match Score: 75%                 │   │
│  ├─────────────────────────────────────┤   │
│  │  ✅ Present: React, Node.js          │   │
│  │  ❌ Missing: Python, AWS             │   │
│  │  💡 Add cloud computing experience   │   │
│  └─────────────────────────────────────┘   │
│                                              │
└─────────────────────────────────────────────┘
```

## 🎯 Feature Map

```
AI Resume Analyzer
│
├── 📤 Upload & Parse
│   ├── PDF Support
│   ├── DOCX Support
│   ├── Text Extraction
│   └── Error Handling
│
├── 🤖 AI Analysis
│   ├── Resume Score (0-100)
│   ├── ATS Score (0-100)
│   ├── 15+ Quality Checks
│   │   ├── Formatting
│   │   ├── Keywords
│   │   ├── Action Verbs
│   │   ├── Readability
│   │   ├── Impact
│   │   └── ... 10 more
│   ├── Weak Bullets
│   ├── Improved Bullets
│   └── Suggestions
│
├── 🎯 Job Matching
│   ├── Keyword Extraction
│   ├── Match Score
│   ├── Missing Keywords
│   ├── Present Keywords
│   ├── Skill Gaps
│   └── Recommendations
│
├── ✨ AI Generation
│   ├── Resume Generator
│   │   ├── Summary
│   │   ├── Experience
│   │   ├── Skills
│   │   └── Education
│   └── Cover Letter
│       ├── Introduction
│       ├── Body
│       └── Conclusion
│
└── 📊 Dashboard
    ├── Upload New
    ├── History
    └── Quick Access
```

## 🔌 API Flow

```
Frontend Request
      ↓
┌─────────────┐
│   Axios     │
│  HTTP Call  │
└─────────────┘
      ↓
┌─────────────┐
│  FastAPI    │
│  Endpoint   │
└─────────────┘
      ↓
┌─────────────┐
│  Validate   │
│   Input     │
└─────────────┘
      ↓
┌─────────────┐
│   Process   │
│  (AI/Parse) │
└─────────────┘
      ↓
┌─────────────┐
│   Database  │
│   (Save)    │
└─────────────┘
      ↓
┌─────────────┐
│   Return    │
│    JSON     │
└─────────────┘
      ↓
Frontend Display
```

## 🎨 Color Scheme

```
Primary Colors:
🔵 Primary Blue:   #0284c7
🟦 Light Blue:     #e0f2fe
⚪ White:          #ffffff
⚫ Dark Gray:      #1f2937

Status Colors:
🟢 Success/Pass:   #16a34a
🟡 Warning:        #eab308
🔴 Error/Fail:     #dc2626

UI Elements:
📦 Cards:          White with shadow
🔘 Buttons:        Primary blue
📝 Inputs:         Gray border
💬 Text:           Dark gray
```

## 📊 Score Visualization

```
Resume Score: 85/100

🟢 80-100:  Excellent
    ████████████████████ 85

🟡 60-79:   Good
    ████████████████░░░░

🔴 0-59:    Needs Work
    ████████░░░░░░░░░░░░
```

## 🗺️ Navigation Map

```
Home (/)
  ├─→ Analyzer (/analyzer)
  ├─→ Job Match (/job-match)
  ├─→ AI Writer (/ai-writer)
  └─→ Dashboard (/dashboard)
```

## 🔄 Data Flow

```
User Input
    ↓
Frontend Validation
    ↓
API Request
    ↓
Backend Processing
    ↓
AI Analysis (OpenAI)
    ↓
Database Storage
    ↓
JSON Response
    ↓
Frontend Display
    ↓
User Action
```

## 🎯 Quick Commands

```bash
# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev

# Docker
docker-compose up -d

# Test
python backend/test_api.py
```

## 📱 Responsive Design

```
Desktop (1024px+)
┌─────────────────────────────┐
│  [Navbar]                   │
│  [Content - 2 Columns]      │
│  [Left Panel] [Right Panel] │
└─────────────────────────────┘

Tablet (768px-1023px)
┌──────────────────┐
│  [Navbar]        │
│  [Content]       │
│  [Full Width]    │
└──────────────────┘

Mobile (< 768px)
┌──────────┐
│ [Nav]    │
│ [Stack]  │
│ [Stack]  │
└──────────┘
```

## 🎓 Learning Path

```
1. START_HERE.md
        ↓
2. QUICKSTART.md
        ↓
3. Run Application
        ↓
4. Test Features
        ↓
5. Read PROJECT_STRUCTURE.md
        ↓
6. Customize Code
        ↓
7. Read DEPLOYMENT.md
        ↓
8. Deploy to Production
        ↓
9. 🎉 Launch!
```

---

## 🚀 Ready to Start?

**Begin with**: [START_HERE.md](START_HERE.md)

**Quick Setup**: [QUICKSTART.md](QUICKSTART.md)

**Full Docs**: [README.md](README.md)

---

*Visual guide for AI Resume Analyzer*
