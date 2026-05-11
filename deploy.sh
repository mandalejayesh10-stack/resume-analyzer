#!/bin/bash

# Resume Analyzer - Production Deployment Helper

set -e

echo "🚀 Resume Analyzer - Deployment Helper"
echo "======================================"
echo ""

# Check environment
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found in root directory"
    echo "Please create .env with required variables:"
    echo "  OPENAI_API_KEY=xxx"
    echo "  DATABASE_URL=xxx"
    echo "  RENDER_API_KEY=xxx"
    exit 1
fi

# Load environment
source .env

echo "📋 Deployment Configuration:"
echo "  Backend: resume-analyzer-backend"
echo "  Frontend: resume-analyzer-app"
echo "  Region: Ohio (Render)"
echo ""

# Check required secrets
if [ -z "$RENDER_API_KEY" ]; then
    echo "❌ RENDER_API_KEY not set in .env"
    echo "Get it from: https://dashboard.render.com/account/api-tokens"
    exit 1
fi

if [ -z "$VERCEL_TOKEN" ]; then
    echo "⚠️  VERCEL_TOKEN not set - frontend deployment will be skipped"
    echo "Get it from: https://vercel.com/account/tokens"
fi

echo "✅ Configuration verified"
echo ""

# Verify code is committed
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  You have uncommitted changes. Push them first:"
    echo "   git add ."
    echo "   git commit -m 'pre-deployment'"
    echo "   git push"
    exit 1
fi

echo "✅ Code is committed"
echo ""

echo "📤 Deployment Instructions:"
echo ""
echo "Option 1: Automatic CI/CD (Recommended)"
echo "  - GitHub Actions will deploy automatically"
echo "  - Just push to main branch"
echo "  - Visit: https://github.com/yourusername/resume-analyzer/actions"
echo ""

echo "Option 2: Manual Deployment"
echo "  Backend (Render):"
echo "    curl -X POST https://api.render.com/deploy/srv-\$SERVICE_ID?key=\$RENDER_API_KEY"
echo ""
echo "  Frontend (Vercel):"
echo "    vercel --prod --token \$VERCEL_TOKEN"
echo ""

echo "✅ Ready to deploy!"
echo ""
echo "Next step: Push your code and check GitHub Actions"
