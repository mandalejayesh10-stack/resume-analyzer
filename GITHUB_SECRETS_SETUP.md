# 🔐 GitHub Secrets Setup Guide - CI/CD Deployment

## What You Need to Do

To enable automatic deployment via GitHub Actions, you need to add deployment credentials as GitHub Secrets.

---

## 📋 Secrets You Need to Add

| Secret | Where to Get | Required |
|--------|-------------|----------|
| `RENDER_API_KEY` | Render Dashboard | ✅ Yes |
| `RENDER_SERVICE_ID` | Render Dashboard | ✅ Yes |
| `VERCEL_TOKEN` | Vercel Account | ✅ Yes |
| `VERCEL_ORG_ID` | Vercel Account | ✅ Yes |
| `VERCEL_PROJECT_ID` | Vercel Account | ✅ Yes |
| `OPENAI_API_KEY` | OpenAI Platform | ⭐ Optional |

---

## 🔑 How to Get Each Secret

### 1. RENDER_API_KEY

1. Go to: https://dashboard.render.com/account/api-tokens
2. Click **"Create API Key"**
3. Give it a name: `GitHub Actions`
4. Click **"Create"**
5. Copy the key
6. ✅ Use this as `RENDER_API_KEY` in GitHub Secrets

### 2. RENDER_SERVICE_ID

1. Go to: https://dashboard.render.com
2. Find your service: `resume-analyzer-backend`
3. Open it
4. Look at the URL: `https://dashboard.render.com/srv-xxxxxx`
5. Copy the `srv-xxxxxx` part
6. ✅ Use this as `RENDER_SERVICE_ID` in GitHub Secrets

### 3. VERCEL_TOKEN

1. Go to: https://vercel.com/account/tokens
2. Click **"Create"**
3. Give it a name: `GitHub Actions`
4. Set expiration: 90 days (or longer)
5. Click **"Create Token"**
6. Copy the token
7. ✅ Use this as `VERCEL_TOKEN` in GitHub Secrets

### 4. VERCEL_ORG_ID

1. Go to: https://vercel.com/account/settings
2. Look for **"Team ID"** or **"User ID"**
3. Copy it
4. ✅ Use this as `VERCEL_ORG_ID` in GitHub Secrets

### 5. VERCEL_PROJECT_ID

1. Go to: https://vercel.com/dashboard
2. Find your project: `resume-analyzer-app`
3. Click it
4. Go to **Settings** → **General**
5. Look for **"Project ID"**
6. Copy it
7. ✅ Use this as `VERCEL_PROJECT_ID` in GitHub Secrets

### 6. OPENAI_API_KEY (Optional)

1. Go to: https://platform.openai.com/api-keys
2. Click **"Create new secret key"**
3. Give it a name: `Resume Analyzer`
4. Copy the key (only shown once!)
5. ✅ Use this as `OPENAI_API_KEY` in GitHub Secrets

> **Note:** If you don't add this, AI features won't work but the app will still function

---

## 🔒 Adding Secrets to GitHub

### Method 1: GitHub Web Interface (Recommended)

1. Go to your GitHub repository
2. Click **Settings** (top right)
3. Click **Secrets and variables** → **Actions**
4. Click **"New repository secret"**
5. Fill in:
   - **Name:** (e.g., `RENDER_API_KEY`)
   - **Value:** (paste the key you got above)
6. Click **"Add secret"**
7. Repeat for each secret

### Method 2: GitHub CLI

```bash
# Install GitHub CLI first: https://cli.github.com

# Login
gh auth login

# Add secrets
gh secret set RENDER_API_KEY -b "your_key_here"
gh secret set RENDER_SERVICE_ID -b "srv-xxxxx"
gh secret set VERCEL_TOKEN -b "your_token_here"
gh secret set VERCEL_ORG_ID -b "your_org_id"
gh secret set VERCEL_PROJECT_ID -b "your_project_id"
gh secret set OPENAI_API_KEY -b "sk-proj-xxxxx" # Optional
```

---

## ✅ Verify Secrets Were Added

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. You should see all your secrets listed
4. ✅ Secrets are set (content hidden for security)

---

## 🚀 Now Deploy!

Once secrets are added:

1. Make a change to your code
2. Push to main: `git push`
3. Go to **Actions** tab in GitHub
4. Watch the deployment workflow run
5. Check Render and Vercel dashboards

---

## 📊 Workflow Files

GitHub Actions workflows are configured in:

- `.github/workflows/deploy-backend.yml` - Deploy to Render
- `.github/workflows/deploy-frontend.yml` - Deploy to Vercel

These run automatically when you push to main.

---

## 🔍 Troubleshooting

### Workflow Fails
- Check GitHub Actions logs: **Actions** tab → **Workflow name** → **Latest run**
- Common issues:
  - Wrong secret name (must match exactly)
  - Invalid token (expired or revoked)
  - Missing service ID

### Deployment Doesn't Start
- Check if secrets are added: Settings → Secrets
- Check if file changed (workflow only runs if relevant files changed)
- Try pushing a change to trigger workflow

### Can't Find Secret Values
- **Render API Key:** https://dashboard.render.com/account/api-tokens
- **Render Service ID:** In service details URL
- **Vercel Token:** https://vercel.com/account/tokens
- **Vercel IDs:** Project Settings → General

---

## 🎉 Complete!

Once secrets are added and code is pushed:

```
GitHub → push code → Actions runs → Render deploys → Vercel deploys → ✅ Live!
```

**Automatic deployment is now enabled!** 🚀

---

## 📞 Quick Checklist

- [ ] Added RENDER_API_KEY
- [ ] Added RENDER_SERVICE_ID
- [ ] Added VERCEL_TOKEN
- [ ] Added VERCEL_ORG_ID
- [ ] Added VERCEL_PROJECT_ID
- [ ] (Optional) Added OPENAI_API_KEY
- [ ] Verified secrets in Settings → Secrets
- [ ] Pushed code to main
- [ ] Checked Actions tab
- [ ] Deployment completed

---

**All set! Your app will deploy automatically now.** ✨
