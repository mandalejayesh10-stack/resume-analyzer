# 🚀 Complete Deployment Guide - Resume Analyzer

## Step 1: Prepare Your OpenAI API Key

**Time: 5 minutes**

1. Go to: https://platform.openai.com/api-keys
2. Create a new API key (or use existing)
3. Copy and save it somewhere safe
4. **Cost**: $5-20/month (pay-as-you-go, free tier available)

> **Note:** If you don't have an API key yet, you can deploy without it and the app will still work (just without AI features).

---

## Step 2: Deploy Backend to Render ✅

**Time: 10 minutes**

### 2.1 Go to Render Dashboard
- Visit: https://dashboard.render.com
- Sign up (free account)
- Connect your GitHub account

### 2.2 Create Backend Service
1. Click **"New +"** → **"Web Service"**
2. Select **"Deploy an existing repository"**
3. Find and select **`resume-analyzer`** repository
4. Click **"Connect"**

### 2.3 Configure Service
Fill in these exact settings:

```
Name:                resume-analyzer-backend
Environment:         Python 3
Region:              Ohio (or closest to you)
Branch:              main
Root Directory:      (leave empty)
Build Command:       pip install -r backend/requirements.txt
Start Command:       uvicorn backend.main:app --host 0.0.0.0 --port 10000
Plan:                Free
```

### 2.4 Add Environment Variables
Click **"Advanced"** section:

```
OPENAI_API_KEY       = [your API key from Step 1]
DATABASE_URL         = sqlite:///./resume_analyzer.db
CORS_ORIGINS         = *
```

### 2.5 Deploy
- Click **"Create Web Service"**
- Wait 3-5 minutes for deployment
- Once live, you'll see a URL like: `https://resume-analyzer-backend.onrender.com`
- **Test it:** Visit `https://resume-analyzer-backend.onrender.com/docs`

---

## Step 3: Deploy Frontend to Vercel ✅

**Time: 10 minutes**

### 3.1 Go to Vercel Dashboard
- Visit: https://vercel.com
- Sign up (free account)
- Connect your GitHub account

### 3.2 Create Frontend Project
1. Click **"Add New"** → **"Project"**
2. Select **`resume-analyzer`** repository
3. Click **"Import"**

### 3.3 Configure Project
Fill in these settings:

```
Project Name:        resume-analyzer-frontend
Framework:           Next.js
Root Directory:      frontend
Environment:         Node.js (default)
```

### 3.4 Add Environment Variables
Add this environment variable:

```
NEXT_PUBLIC_API_URL = https://resume-analyzer-backend.onrender.com
```

⚠️ **IMPORTANT:** The variable name must start with `NEXT_PUBLIC_` so it's available in the browser.

### 3.5 Deploy
- Click **"Deploy"**
- Wait 2-3 minutes
- You'll get a URL like: `https://resume-analyzer-frontend.vercel.app`
- **Test it:** Visit that URL in your browser

---

## Step 4: Verify Deployment ✅

**Time: 5 minutes**

### Backend Verification
Visit: `https://resume-analyzer-backend.onrender.com/docs`
- Should see Swagger UI
- Click "Try it out" on any endpoint

### Frontend Verification
Visit your Vercel URL
- Should see the landing page
- Try uploading a resume
- Test all pages

---

## Step 5: Post-Deployment Checklist ✅

- [ ] Backend deployed to Render (has /docs working)
- [ ] Frontend deployed to Vercel (shows landing page)
- [ ] Can upload files from frontend
- [ ] Can see analysis results
- [ ] AI features work (if API key added)
- [ ] No console errors

---

## 🔗 Quick Links

| Service | URL |
|---------|-----|
| **Render Dashboard** | https://dashboard.render.com |
| **Vercel Dashboard** | https://vercel.com |
| **OpenAI API Keys** | https://platform.openai.com/api-keys |
| **GitHub Repo** | https://github.com/yourusername/resume-analyzer |

---

## ❌ Troubleshooting

### Backend won't deploy
- Check Build Command: `pip install -r backend/requirements.txt`
- Check Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port 10000`
- Check logs in Render dashboard

### Frontend won't connect to backend
- Verify `NEXT_PUBLIC_API_URL` in Vercel environment variables
- Should be your Render backend URL (without trailing slash)

### AI features not working
- Check if `OPENAI_API_KEY` is set in Render backend
- Verify API key is valid at: https://platform.openai.com/api-keys

### Slow uploads
- Normal for first request (cold start)
- Render free tier has limitations

---

## 💡 Next Steps (Optional)

### After successful deployment:
1. **Custom Domain:** Add your own domain in Vercel settings
2. **Custom Domain for Backend:** Add domain in Render settings
3. **Database:** Upgrade to PostgreSQL for production
4. **Stripe:** Add payment if creating paid tiers
5. **Analytics:** Add monitoring and error tracking

---

## 📞 Support

If you get stuck:
1. Check the service logs (visible in Render/Vercel dashboard)
2. Review the error messages
3. Verify environment variables are set correctly
4. Ensure GitHub repo is public or you've connected properly

---

**Good luck! 🎉 Your app will be live in ~20 minutes!**
