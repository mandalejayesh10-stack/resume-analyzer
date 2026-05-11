# ⚡ DEPLOY IN 5 MINUTES

## 🎯 What You Need
- ✅ Render Account (you have it)
- ✅ Vercel Account (you have it)
- ✅ GitHub Account (you have it)
- ✅ OpenAI API Key (in `.env`)

---

## 🚀 DEPLOY STEPS (Copy-Paste Ready)

### **Step 1: Check GitHub Workflows**
Make sure `.github/workflows/` has:
- `deploy-backend.yml` ✅
- `deploy-frontend.yml` ✅

### **Step 2: Add GitHub Secrets**
Go to: `GitHub Repo → Settings → Secrets and variables → Actions`

Add these secrets:
```
OPENAI_API_KEY = sk-proj-G5Gt_HP7rEChs7lj...
RENDER_API_KEY = rnd_yourkeyhere
VERCEL_TOKEN = vercel_yourtokenhere
```

### **Step 3: Push to GitHub**
```bash
cd "c:\Users\JAYESH\Documents\resume analyzer"
git add .
git commit -m "Deploy Resume Analyzer"
git push
```

### **Step 4: Wait for Automation**
GitHub Actions will automatically:
- ✅ Deploy backend to Render
- ✅ Deploy frontend to Vercel
- ✅ Run health checks

---

## 📊 Timeline
| Step | Time | Status |
|------|------|--------|
| Add Secrets | 2 min | Manual |
| Git Push | 1 min | Automatic |
| Backend Deploy | 3 min | Automatic |
| Frontend Deploy | 3 min | Automatic |
| **Total** | **~9 min** | ✅ |

---

## ✅ Success Indicators
- Backend URL: `https://resume-analyzer-backend.onrender.com`
- Frontend URL: `https://resume-analyzer-frontend.vercel.app`
- Both show no errors
- File upload works
- Analysis responds

---

## 🔑 Get Your Keys

### **Render API Key:**
1. Go to https://dashboard.render.com
2. Settings → API Keys
3. Copy key

### **Vercel Token:**
1. Go to https://vercel.com/account/tokens
2. Create new token
3. Copy token

---

## 🎊 That's It!
Push code → GitHub Actions deploy → Your app is live!
