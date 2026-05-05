# Deployment Guide

Complete guide for deploying the AI Resume Analyzer to production.

## Prerequisites

- GitHub account
- Vercel account (for frontend)
- Render/Railway account (for backend)
- Neon/Supabase account (for database)
- OpenAI API key

## Step 1: Database Setup (Neon)

1. Go to https://neon.tech
2. Create new project
3. Create database named `resume_analyzer`
4. Copy connection string (looks like):
   ```
   postgresql://user:password@host.neon.tech/resume_analyzer
   ```
5. Save this for backend configuration

## Step 2: Backend Deployment (Render)

### Option A: Render

1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `ai-resume-analyzer-api`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

5. Add Environment Variables:
   ```
   OPENAI_API_KEY=sk-...
   DATABASE_URL=postgresql://...
   CORS_ORIGINS=https://your-frontend-domain.vercel.app
   ```

6. Click "Create Web Service"
7. Wait for deployment
8. Copy the service URL (e.g., `https://ai-resume-analyzer-api.onrender.com`)

### Option B: Railway

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Python
5. Add Environment Variables:
   ```
   OPENAI_API_KEY=sk-...
   DATABASE_URL=postgresql://...
   CORS_ORIGINS=https://your-frontend-domain.vercel.app
   ```
6. Click "Deploy"
7. Copy the service URL

## Step 3: Frontend Deployment (Vercel)

1. Go to https://vercel.com
2. Click "Add New..." → "Project"
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

5. Add Environment Variables:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-url.onrender.com
   ```

6. Click "Deploy"
7. Wait for deployment
8. Copy the deployment URL

## Step 4: Update CORS

1. Go back to your backend deployment (Render/Railway)
2. Update `CORS_ORIGINS` environment variable:
   ```
   CORS_ORIGINS=https://your-frontend-domain.vercel.app
   ```
3. Redeploy backend

## Step 5: Initialize Database

1. Use Render/Railway shell or local connection:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

Or connect to database directly and run:
```sql
CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    filename VARCHAR NOT NULL,
    content TEXT NOT NULL,
    score FLOAT,
    ats_score FLOAT,
    analysis TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE job_matches (
    id SERIAL PRIMARY KEY,
    resume_id INTEGER NOT NULL,
    job_description TEXT NOT NULL,
    match_score FLOAT NOT NULL,
    missing_keywords TEXT,
    recommendations TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Step 6: Test Deployment

1. Visit your frontend URL
2. Upload a test resume
3. Verify analysis works
4. Test job matching
5. Test AI writer

## Environment Variables Summary

### Backend
```env
OPENAI_API_KEY=sk-proj-...
DATABASE_URL=postgresql://user:pass@host/db
REDIS_URL=redis://host:6379 (optional)
CORS_ORIGINS=https://your-app.vercel.app
```

### Frontend
```env
NEXT_PUBLIC_API_URL=https://your-api.onrender.com
```

## Custom Domain (Optional)

### Frontend (Vercel)
1. Go to Project Settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions

### Backend (Render)
1. Go to Service Settings → Custom Domain
2. Add your custom domain
3. Follow DNS configuration instructions

## Monitoring

### Render
- View logs in dashboard
- Set up health checks
- Configure auto-deploy from GitHub

### Vercel
- View deployment logs
- Analytics available
- Automatic deployments on push

## Troubleshooting

### Backend Issues
- Check logs in Render/Railway dashboard
- Verify environment variables are set
- Ensure database connection string is correct
- Check OpenAI API key is valid

### Frontend Issues
- Check Vercel deployment logs
- Verify `NEXT_PUBLIC_API_URL` is correct
- Test API endpoints directly
- Check browser console for errors

### CORS Issues
- Ensure `CORS_ORIGINS` includes your frontend URL
- Check for trailing slashes
- Verify protocol (http vs https)

### Database Issues
- Verify connection string format
- Check database is accessible
- Ensure tables are created
- Check database logs

## Scaling

### Backend
- Render: Upgrade to higher tier for more resources
- Railway: Automatic scaling available
- Add Redis for caching (optional)

### Frontend
- Vercel: Automatic scaling included
- CDN distribution worldwide
- Edge functions available

### Database
- Neon: Upgrade for more storage/connections
- Enable connection pooling
- Add read replicas if needed

## Cost Estimates

### Free Tier
- Vercel: Free for personal projects
- Render: Free tier available (with limitations)
- Neon: Free tier (0.5GB storage)
- OpenAI: Pay per use (~$0.002 per analysis)

### Production
- Vercel Pro: $20/month
- Render Starter: $7/month
- Neon Pro: $19/month
- OpenAI: ~$50-200/month (depends on usage)

## Security Checklist

✅ Environment variables not in code
✅ CORS properly configured
✅ API key secured
✅ Database credentials secured
✅ HTTPS enabled
✅ File upload validation
✅ Input sanitization
✅ Error messages don't leak sensitive info

## Backup Strategy

1. Database: Neon provides automatic backups
2. Code: GitHub repository
3. Environment variables: Document separately
4. Regular exports of user data

## Updates & Maintenance

1. Monitor error logs regularly
2. Update dependencies monthly
3. Test before deploying
4. Use staging environment for testing
5. Keep OpenAI API updated

---

Your AI Resume Analyzer is now live! 🚀
