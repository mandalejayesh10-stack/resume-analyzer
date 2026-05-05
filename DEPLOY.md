# Deployment Guide - Resume Analyzer

## Prerequisites
- GitHub account (code is already pushed)
- Render.com account (free)
- OpenAI API key (optional - app will start without it, but AI features won't work)

## Step 1: Connect to Render

1. Go to: https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Select **"Deploy an existing repository"**
4. Connect your GitHub account if needed
5. Search and select: `resume-analyzer`
6. Click **"Connect"**

## Step 2: Configure Service

Fill in these settings:

| Field | Value |
|-------|-------|
| **Name** | `resume-analyzer-backend` |
| **Environment** | `Python 3` |
| **Region** | `Ohio` (or closest to you) |
| **Branch** | `main` |
| **Build Command** | `pip install -r backend/requirements.txt` |
| **Start Command** | `uvicorn backend.main:app --host 0.0.0.0 --port 10000` |

## Step 3: Add Environment Variables

Click **"Advanced"** or **"Environment"** and add:

```
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./resume_analyzer.db
REDIS_URL=redis://localhost:6379
CORS_ORIGINS=*
```

**Important:** If you don't have an OpenAI key, leave `OPENAI_API_KEY` empty - the app will still start!

## Step 4: Deploy

Click **"Create Web Service"** and wait 3-5 minutes.

## Step 5: Verify

Once deployed, test these URLs:

- **Root endpoint:** `https://your-service.onrender.com/`
- **API docs:** `https://your-service.onrender.com/docs`
- **Resumes endpoint:** `https://your-service.onrender.com/resumes`

You should see JSON responses from all endpoints.

## Troubleshooting

### "Not Found" Error
- Check the **Logs** tab in Render for error messages
- Make sure `Start Command` path is correct: `uvicorn backend.main:app --host 0.0.0.0 --port 10000`

### Module Import Errors
- Clear cache and redeploy: Click the **"Deploy"** button → **"Clear cache & deploy"**
- Verify `Build Command` points to correct requirements: `pip install -r backend/requirements.txt`

### API Key Errors
- Either add your OpenAI API key to Environment Variables
- Or remove it from code if not needed (app will start without it)

## API Endpoints

Once deployed, you can use:

```bash
# Test root endpoint
curl https://your-service.onrender.com/

# Get all resumes
curl https://your-service.onrender.com/resumes

# Upload resume (requires file)
curl -F "file=@resume.pdf" https://your-service.onrender.com/upload
```

## Frontend Integration

After backend is deployed, update your frontend `.env.local`:

```
NEXT_PUBLIC_API_URL=https://your-service.onrender.com
```

Then redeploy frontend pointing to this backend URL.
