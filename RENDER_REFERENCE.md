# RENDER DEPLOYMENT - COPY & PASTE VALUES

## GitHub Login
1. Go: https://dashboard.render.com
2. Click: GitHub (login with your account)

## Create Web Service
1. Click: "New +" → "Web Service"
2. Select: "resume-analyzer" repo
3. Click: "Connect"

---

## FORM FIELDS TO FILL:

### Basic Settings
```
Name:              resume-analyzer-backend
Environment:       Python 3
Region:            Ohio (or closest to you)
Branch:            main
```

### Commands
```
Build Command:     pip install -r backend/requirements.txt

Start Command:     uvicorn backend.main:app --host 0.0.0.0 --port 10000
```

### Plan
```
Select: Free (or Paid for production)
```

---

## ENVIRONMENT VARIABLES

Click "Advanced" or "Environment" tab and add these:

```
Key: OPENAI_API_KEY
Value: (your OpenAI API key or leave blank)

Key: DATABASE_URL  
Value: sqlite:///./resume_analyzer.db

Key: REDIS_URL
Value: redis://localhost:6379

Key: CORS_ORIGINS
Value: *
```

---

## DEPLOYMENT

1. Click: "Create Web Service"
2. Wait: 3-5 minutes
3. Watch: "Logs" tab for progress

---

## VERIFY IT WORKS

After deployment succeeds, open:

```
https://your-service-name.onrender.com/
```

You should see JSON response:
```json
{
  "message": "AI Resume Analyzer API",
  "status": "running"
}
```

For API documentation:
```
https://your-service-name.onrender.com/docs
```

You should see Swagger UI (interactive API docs)

---

## TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| "Not Found" error | Check Logs tab, verify Start Command is correct |
| Build fails | Clear cache, redeploy |
| Module not found | Verify Build Command path: `backend/requirements.txt` |
| App crashes on start | Check environment variables are set |

---

## AFTER BACKEND IS LIVE

Update frontend `.env.local`:

```
NEXT_PUBLIC_API_URL=https://your-service-name.onrender.com
```

Then redeploy frontend.
