# ⚡ DO THIS NOW - 5 MINUTE DEPLOYMENT

## 🎯 You're Here. Everything Works. Just Do This:

---

## Step 1️⃣: Open GitHub Secrets
```
https://github.com/mandalejayesh10-stack/resume-analyzer/settings/secrets/actions
```

## Step 2️⃣: Add 5 Secrets

### Secret #1
```
Name: RENDER_API_KEY
Value: [Get from https://dashboard.render.com/settings/api-keys]
```

### Secret #2
```
Name: RENDER_SERVICE_ID
Value: srv-xxxxxxxxxxxxxxxxx
[Get from your Render service URL]
```

### Secret #3
```
Name: VERCEL_TOKEN
Value: [Get from https://vercel.com/account/tokens]
```

### Secret #4
```
Name: VERCEL_ORG_ID
Value: team_xxxxxxxxxxxxxxxx
[Get from https://vercel.com/account/settings]
```

### Secret #5
```
Name: VERCEL_PROJECT_ID
Value: [Get from Vercel Project Settings]
```

---

## Step 3️⃣: GitHub Actions Deploy Automatically ✅

After adding secrets:
- Next push triggers deployment
- Backend → Render
- Frontend → Vercel
- Takes ~10 minutes

---

## 📊 Time Breakdown
```
Getting keys:     3 min
Adding secrets:   2 min
Deployment runs:  10 min (automatic)
----
Total:           15 min
```

---

## ✅ When It's Done

✅ Backend: `https://resume-analyzer-backend.onrender.com`
✅ Frontend: `https://resume-analyzer-frontend.vercel.app`
✅ Both: Working and connected

---

## 🚀 That's It!
Just add the secrets and you're done!
