"""
Production Readiness Verification Script
Validates that the backend is ready for Render deployment
"""

import os
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))

def verify_files():
    """Check that all required files exist"""
    required_files = [
        "backend/main.py",
        "backend/config.py",
        "backend/database.py",
        "backend/ai_analyzer.py",
        "backend/file_parser.py",
        "backend/requirements.txt",
        ".gitignore",
        "Procfile",
        "render.yaml",
    ]
    
    print("📁 Checking required files...")
    missing = []
    for file in required_files:
        if not Path(file).exists():
            missing.append(file)
            print(f"  ❌ {file}")
        else:
            print(f"  ✅ {file}")
    
    return len(missing) == 0

def verify_config():
    """Check that config loads without errors"""
    print("\n⚙️  Checking configuration...")
    try:
        from config import settings
        print(f"  ✅ Config loads successfully")
        print(f"     - Database: {settings.database_url}")
        print(f"     - CORS Origins: {settings.cors_origins}")
        print(f"     - API Key set: {'Yes' if settings.openai_api_key else 'No (optional)'}")
        return True
    except Exception as e:
        print(f"  ❌ Config error: {e}")
        return False

def verify_fastapi():
    """Check that FastAPI app initializes"""
    print("\n🚀 Checking FastAPI app...")
    try:
        from main import app
        print(f"  ✅ FastAPI app loads successfully")
        print(f"     - Routes: {len(app.routes)}")
        print(f"     - Middleware: {len(app.user_middleware)}")
        return True
    except Exception as e:
        print(f"  ❌ FastAPI error: {e}")
        return False

def verify_dependencies():
    """Check that all dependencies are in requirements.txt"""
    print("\n📦 Checking dependencies...")
    try:
        with open("backend/requirements.txt", "r") as f:
            deps = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        
        required = [
            "fastapi",
            "uvicorn",
            "python-multipart",
            "openai",
            "sqlalchemy",
            "pydantic",
            "pdfplumber",
            "python-docx",
        ]
        
        missing = []
        for dep in required:
            # Check if dependency name is in requirements (handles version numbers)
            if not any(dep in line.lower() for line in deps):
                missing.append(dep)
        
        if missing:
            print(f"  ❌ Missing dependencies: {missing}")
            return False
        else:
            print(f"  ✅ All required dependencies present")
            for dep in deps:
                print(f"     - {dep}")
            return True
    except Exception as e:
        print(f"  ❌ Dependencies check error: {e}")
        return False

def verify_environment():
    """Check environment variables"""
    print("\n🔑 Checking environment variables...")
    required_env = {
        "OPENAI_API_KEY": "Optional (leave blank if no key)",
        "DATABASE_URL": "Required",
        "CORS_ORIGINS": "Required",
    }
    
    missing_required = []
    for var, status in required_env.items():
        value = os.getenv(var, "")
        if value:
            print(f"  ✅ {var} = {value[:30]}...")
        else:
            print(f"  ⚠️  {var} = (not set) - {status}")
            if "Required" in status:
                missing_required.append(var)
    
    return len(missing_required) == 0

def main():
    print("=" * 60)
    print("Resume Analyzer - Production Readiness Check")
    print("=" * 60)
    
    os.chdir(Path(__file__).parent)
    
    results = {
        "Files": verify_files(),
        "Config": verify_config(),
        "FastAPI": verify_fastapi(),
        "Dependencies": verify_dependencies(),
        "Environment": verify_environment(),
    }
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    for check, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{check}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 APPLICATION IS PRODUCTION READY!")
        print("\nNext steps:")
        print("1. Go to: https://dashboard.render.com")
        print("2. Create new Web Service")
        print("3. Select: resume-analyzer repo")
        print("4. Use settings from RENDER_REFERENCE.md")
        print("5. Deploy!")
    else:
        print("⚠️  Please fix the failed checks above before deploying")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
