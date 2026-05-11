#!/bin/bash
# Resume Analyzer - Complete Automated Deployment Script
# This script handles the entire deployment process

set -e

echo "🚀 Resume Analyzer - Automated Deployment"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if running on Windows (Git Bash/WSL) or native Linux/Mac
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo "⚠️ Please use deploy.bat for Windows"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Step 1: Verify Prerequisites
echo -e "${BLUE}📋 Step 1: Verifying Prerequisites${NC}"
echo ""

if ! command_exists git; then
    echo -e "${RED}❌ Git is required but not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Git found${NC}"

if ! command_exists python3; then
    echo -e "${RED}❌ Python 3 is required but not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python 3 found${NC}"

if ! command_exists node; then
    echo -e "${RED}❌ Node.js is required but not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Node.js found${NC}"

echo ""

# Step 2: Verify Git Repository
echo -e "${BLUE}📋 Step 2: Verifying Git Repository${NC}"
echo ""

if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}❌ Not a git repository${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Git repository found${NC}"

REPO_NAME=$(basename "$(git rev-parse --show-toplevel)")
echo "Repository: $REPO_NAME"

# Check if code is committed
if [[ -n $(git status --porcelain) ]]; then
    echo -e "${YELLOW}⚠️ You have uncommitted changes${NC}"
    echo "Committing changes..."
    git add .
    git commit -m "deployment: automated deployment setup" || true
fi

echo ""

# Step 3: Setup Backend
echo -e "${BLUE}📋 Step 3: Setting Up Backend${NC}"
echo ""

cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate || . venv/Scripts/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -q -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating backend .env file..."
    cat > .env << EOF
OPENAI_API_KEY=
DATABASE_URL=sqlite:///./resume_analyzer.db
CORS_ORIGINS=*
EOF
fi

echo -e "${GREEN}✅ Backend setup complete${NC}"
cd ..

echo ""

# Step 4: Setup Frontend
echo -e "${BLUE}📋 Step 4: Setting Up Frontend${NC}"
echo ""

cd frontend

echo "Installing Node.js dependencies..."
npm install -q

# Create .env.local if it doesn't exist
if [ ! -f ".env.local" ]; then
    echo "Creating frontend .env.local file..."
    cat > .env.local << EOF
NEXT_PUBLIC_API_URL=http://localhost:8000
EOF
fi

echo -e "${GREEN}✅ Frontend setup complete${NC}"
cd ..

echo ""

# Step 5: Verify Deployment Configuration
echo -e "${BLUE}📋 Step 5: Verifying Deployment Configuration${NC}"
echo ""

# Check required files
required_files=(
    "render.yaml"
    "vercel.json"
    ".github/workflows/deploy-backend.yml"
    ".github/workflows/deploy-frontend.yml"
)

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✅ $file exists${NC}"
    else
        echo -e "${RED}❌ $file not found${NC}"
    fi
done

echo ""

# Step 6: Setup GitHub Secrets (Interactive)
echo -e "${BLUE}📋 Step 6: GitHub Secrets Setup${NC}"
echo ""

echo "You need to add these secrets to your GitHub repository:"
echo ""
echo "Go to: https://github.com/yourusername/resume-analyzer/settings/secrets/actions"
echo ""

secrets_needed=(
    "RENDER_API_KEY"
    "RENDER_SERVICE_ID"
    "VERCEL_TOKEN"
    "VERCEL_ORG_ID"
    "VERCEL_PROJECT_ID"
    "OPENAI_API_KEY"
)

for secret in "${secrets_needed[@]}"; do
    echo -e "${YELLOW}$secret${NC} - Get instructions at:"
    case $secret in
        RENDER_API_KEY)
            echo "  https://dashboard.render.com/account/api-tokens"
            ;;
        RENDER_SERVICE_ID)
            echo "  https://dashboard.render.com (look at service URL)"
            ;;
        VERCEL_TOKEN)
            echo "  https://vercel.com/account/tokens"
            ;;
        VERCEL_ORG_ID)
            echo "  https://vercel.com/account/settings"
            ;;
        VERCEL_PROJECT_ID)
            echo "  https://vercel.com/dashboard (project settings)"
            ;;
        OPENAI_API_KEY)
            echo "  https://platform.openai.com/api-keys (optional)"
            ;;
    esac
    echo ""
done

read -p "Have you added all the secrets? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Please add the secrets and run this script again"
    exit 1
fi

echo ""

# Step 7: Push to GitHub
echo -e "${BLUE}📋 Step 7: Pushing to GitHub${NC}"
echo ""

echo "Current branch:"
git branch --show-current

read -p "Ready to push to GitHub? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Pushing to GitHub..."
    git push origin main
    echo -e "${GREEN}✅ Pushed to GitHub${NC}"
else
    echo "Push cancelled"
fi

echo ""

# Step 8: Watch GitHub Actions
echo -e "${BLUE}📋 Step 8: GitHub Actions Deployment${NC}"
echo ""

echo "Your deployment is now running!"
echo ""
echo "Watch it at:"
echo -e "${YELLOW}https://github.com/yourusername/resume-analyzer/actions${NC}"
echo ""
echo "Check deployment status at:"
echo -e "${YELLOW}Render: https://dashboard.render.com${NC}"
echo -e "${YELLOW}Vercel: https://vercel.com/dashboard${NC}"
echo ""

echo -e "${GREEN}✅ Deployment setup complete!${NC}"
echo ""
echo "🎉 Your app will be live in 5-10 minutes!"
