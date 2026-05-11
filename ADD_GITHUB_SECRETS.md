# 🔐 ADD GITHUB SECRETS FOR AUTOMATIC DEPLOYMENT

## ⚠️ IMPORTANT: Add These Secrets to Deploy Successfully!

Your workflows need GitHub secrets to deploy. It takes **2 minutes**.

---

## 🎯 Go to GitHub Secrets

1. Open: `https://github.com/mandalejayesh10-stack/resume-analyzer`
2. Click: **Settings** (top menu)
3. Click: **Secrets and variables** (left sidebar)
4. Click: **Actions**

---

## 🔑 Required Secrets

### **For Render Backend Deployment**

#### Secret 1: RENDER_API_KEY
```
Name: RENDER_API_KEY
Value: [Get from Render dashboard]

How to get:
1. Go: https://dashboard.render.com
2. Click: Settings
3. Click: API Keys
4. Copy your API key
```

#### Secret 2: RENDER_SERVICE_ID
```
Name: RENDER_SERVICE_ID
Value: srv-xxxxxxxxxxxxxxxx [Get from your Render service]

How to get:
1. Go: https://dashboard.render.com
2. Click your "Resume Analyzer Backend" service
3. URL bar shows: https://dashboard.render.com/services/srv-xxxxx
4. Copy the service ID
```

---

### **For Vercel Frontend Deployment**

#### Secret 1: VERCEL_TOKEN
```
Name: VERCEL_TOKEN
Value: [Get from Vercel]

How to get:
1. Go: https://vercel.com/account/tokens
2. Create New Token
3. Copy the token
```

#### Secret 2: VERCEL_ORG_ID
```
Name: VERCEL_ORG_ID
Value: [Get from Vercel]

How to get:
1. Go: https://vercel.com/account/settings
2. Copy "Team ID" (shown as org-xxxxx)
```

#### Secret 3: VERCEL_PROJECT_ID
```
Name: VERCEL_PROJECT_ID
Value: [Get from Vercel project settings]

How to get:
1. Go: https://vercel.com/dashboard
2. Click your "Resume Analyzer" project
3. Click: Settings
4. Copy "Project ID"
```

---

## ✅ Quick Add Process

### **To add each secret:**
1. Click: **New repository secret**
2. Type: Secret name (exactly as shown)
3. Type: Secret value (paste from above)
4. Click: **Add secret**
5. Repeat for all secrets

---

## 📊 Summary of All Secrets

| Secret Name | Where to Get | Priority |
|-------------|-------------|----------|
| RENDER_API_KEY | Render Dashboard | ✅ Must Have |
| RENDER_SERVICE_ID | Render Service URL | ✅ Must Have |
| VERCEL_TOKEN | Vercel Account | ✅ Must Have |
| VERCEL_ORG_ID | Vercel Settings | ✅ Must Have |
| VERCEL_PROJECT_ID | Vercel Project | ✅ Must Have |

---

## ⏱️ Time Estimate

```
Getting Render keys: 1 min
Getting Vercel keys: 1 min
Adding to GitHub: 1 min
--
Total: 3 minutes
```

---

## 🚀 After Adding Secrets

1. ✅ Secrets are in GitHub
2. ✅ Next push will trigger deployment
3. ✅ Workflows will use the secrets
4. ✅ Your app deploys automatically!

---

## 🔄 What Happens After Secrets

### **First Deployment**
- Backend builds and deploys to Render
- Frontend builds and deploys to Vercel
- Takes ~10 minutes total

### **Future Deployments**
- Just push code
- GitHub Actions run automatically
- No manual steps needed!

---

## ✨ You're Almost Done!

1. ⏳ Add the 5 secrets (2 min)
2. ✅ Push code (already done)
3. ✅ GitHub Actions deploy (automatic)
4. ✅ App is LIVE! 🎉

---

## 📞 Don't Have the Keys?

### **If you don't have a Render service yet:**
```
1. Go: https://dashboard.render.com
2. Create new Web Service
3. Connect to GitHub repo
4. Get SERVICE_ID from URL
```

### **If you don't have a Vercel project yet:**
```
1. Go: https://vercel.com
2. Import GitHub repo
3. Get TOKEN, ORG_ID, PROJECT_ID from settings
```

---

## 🎊 Summary

1. Add 5 secrets to GitHub (2 min)
2. Your app auto-deploys
3. Everything works!

**That's it! You're done!** 🚀
