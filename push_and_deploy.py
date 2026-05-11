#!/usr/bin/env python3
"""
⚡ FAST DEPLOYMENT SCRIPT
Pushes code to GitHub → Triggers GitHub Actions → App goes live!
"""

import subprocess
import sys

def run_cmd(cmd, description):
    """Run command and show status"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - OK")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        print(e.stderr)
        return False

def main():
    print("\n" + "="*50)
    print("  🚀 RESUME ANALYZER - FAST DEPLOYMENT")
    print("="*50)
    
    # Step 1: Check Git
    print("\n📋 Step 1: Checking Git Status")
    run_cmd("git status", "Git status")
    
    # Step 2: Add all files
    print("\n📋 Step 2: Staging Changes")
    run_cmd("git add .", "Add all files")
    
    # Step 3: Commit
    print("\n📋 Step 3: Committing Changes")
    run_cmd('git commit -m "🚀 Deploy Resume Analyzer with automation"', "Commit")
    
    # Step 4: Push to GitHub
    print("\n📋 Step 4: Pushing to GitHub")
    if run_cmd("git push origin main", "Push to GitHub"):
        print("\n" + "="*50)
        print("  ✅ CODE PUSHED TO GITHUB!")
        print("="*50)
        print("\n🤖 GitHub Actions will now:")
        print("   1. Deploy backend to Render (3 min)")
        print("   2. Deploy frontend to Vercel (3 min)")
        print("   3. Run health checks")
        print("\n⏱️  Total time: ~10 minutes")
        print("\n📍 Check status at:")
        print("   GitHub: https://github.com/your-username/resume-analyzer/actions")
        print("   Backend: https://dashboard.render.com")
        print("   Frontend: https://vercel.com/dashboard")
        print("\n✨ Your app will be live soon!")
    else:
        print("\n❌ Failed to push. Check your GitHub credentials.")
        sys.exit(1)

if __name__ == "__main__":
    main()
