#!/usr/bin/env python3
"""
Resume Analyzer - Master Deployment Coordinator
Orchestrates the entire deployment process
"""

import os
import sys
import subprocess
import time
import platform
from pathlib import Path

class DeploymentCoordinator:
    def __init__(self):
        self.root_dir = Path.cwd()
        self.is_windows = platform.system() == 'Windows'
        self.is_linux = platform.system() == 'Linux'
        self.is_mac = platform.system() == 'Darwin'
        
    def print_banner(self):
        """Print welcome banner"""
        print("\n" + "="*70)
        print(" " * 15 + "🚀 RESUME ANALYZER - DEPLOYMENT COORDINATOR")
        print("="*70 + "\n")
    
    def menu(self):
        """Display main menu"""
        print("\n" + "-"*70)
        print("DEPLOYMENT OPTIONS")
        print("-"*70)
        print("""
1. Quick Start - Setup & Launch Locally
   └─ Installs dependencies and starts both servers

2. Automated Deployment - One-Command Deploy
   └─ Sets up everything and pushes to GitHub

3. Health Check - Verify Installation
   └─ Tests backend and frontend health

4. Manual Deployment - Step by Step
   └─ Opens manual deployment guide

5. Development Mode - Development Setup
   └─ Sets up local development environment

6. Clean Build - Fresh Installation
   └─ Removes node_modules/venv and reinstalls

7. Push to GitHub - Git Operations
   └─ Commits and pushes changes

8. Exit
   └─ Quit the coordinator
""")
        print("-"*70)
        return input("\nSelect option (1-8): ").strip()
    
    def quick_start(self):
        """Quick start - setup and launch"""
        print("\n📋 QUICK START MODE")
        print("="*70)
        print("This will:")
        print("  1. Install Python and Node.js dependencies")
        print("  2. Create environment files")
        print("  3. Start backend server (uvicorn)")
        print("  4. Start frontend server (npm)")
        print("  5. Run health checks")
        
        response = input("\nContinue? (y/n): ").strip().lower()
        if response != 'y':
            return
        
        # Setup backend
        print("\n📦 Setting up backend...")
        backend_dir = self.root_dir / 'backend'
        
        if self.is_windows:
            venv_path = backend_dir / 'venv' / 'Scripts' / 'python.exe'
        else:
            venv_path = backend_dir / 'venv' / 'bin' / 'python'
        
        if not venv_path.exists():
            print("  Creating virtual environment...")
            subprocess.run([sys.executable, '-m', 'venv', str(backend_dir / 'venv')],
                         check=True, capture_output=True)
        
        print("  Installing dependencies...")
        pip_exe = backend_dir / ('venv/Scripts/pip' if self.is_windows else 'venv/bin/pip')
        subprocess.run([str(pip_exe), 'install', '-q', '-r', 'requirements.txt'],
                      cwd=str(backend_dir), check=True)
        
        # Create .env
        env_file = backend_dir / '.env'
        if not env_file.exists():
            env_file.write_text(
                "OPENAI_API_KEY=\n"
                "DATABASE_URL=sqlite:///./resume_analyzer.db\n"
                "CORS_ORIGINS=*\n"
            )
        
        print("  ✅ Backend ready")
        
        # Setup frontend
        print("\n📦 Setting up frontend...")
        frontend_dir = self.root_dir / 'frontend'
        
        if not (frontend_dir / 'node_modules').exists():
            print("  Installing dependencies...")
            subprocess.run(['npm', 'install', '-q'], cwd=str(frontend_dir), check=True)
        
        # Create .env.local
        env_file = frontend_dir / '.env.local'
        if not env_file.exists():
            env_file.write_text("NEXT_PUBLIC_API_URL=http://localhost:8000\n")
        
        print("  ✅ Frontend ready")
        
        # Start servers
        print("\n🚀 Starting servers...")
        
        if self.is_windows:
            print("\n  Backend starting at http://localhost:8000")
            print("  Frontend starting at http://localhost:3000")
            print("\n  To stop servers, press Ctrl+C in each terminal\n")
            
            # Open in separate windows
            backend_cmd = f"cd backend && venv\\Scripts\\activate && uvicorn main:app --reload"
            frontend_cmd = f"cd frontend && npm run dev"
            
            print("  Opening backend terminal...")
            os.system(f"start cmd /k \"{backend_cmd}\"")
            
            time.sleep(3)
            
            print("  Opening frontend terminal...")
            os.system(f"start cmd /k \"{frontend_cmd}\"")
        else:
            print("\n  Run these commands in separate terminals:\n")
            print("  Terminal 1 (Backend):")
            print("    cd backend")
            print("    source venv/bin/activate")
            print("    uvicorn main:app --reload\n")
            print("  Terminal 2 (Frontend):")
            print("    cd frontend")
            print("    npm run dev\n")
        
        # Wait and health check
        print("  Waiting for servers to start (30 seconds)...")
        time.sleep(30)
        
        print("\n🏥 Running health check...")
        subprocess.run([sys.executable, 'health_check.py'])
    
    def automated_deployment(self):
        """Automated deployment"""
        print("\n⚡ AUTOMATED DEPLOYMENT MODE")
        print("="*70)
        
        if self.is_windows:
            script = 'deploy-auto.bat'
        else:
            script = 'deploy-auto.sh'
        
        script_path = self.root_dir / script
        
        if script_path.exists():
            if self.is_windows:
                os.system(str(script_path))
            else:
                subprocess.run(['bash', str(script_path)])
        else:
            print(f"❌ {script} not found")
    
    def health_check(self):
        """Run health check"""
        print("\n🏥 HEALTH CHECK MODE")
        print("="*70)
        
        subprocess.run([sys.executable, 'health_check.py'])
    
    def manual_deployment(self):
        """Show manual deployment guide"""
        print("\n📖 MANUAL DEPLOYMENT")
        print("="*70)
        
        guides = [
            ("START_DEPLOYMENT.md", "Quick overview"),
            ("CI_CD_SETUP.md", "Automatic deployment"),
            ("DEPLOY_NOW.md", "Manual deployment"),
            ("GITHUB_SECRETS_SETUP.md", "Getting API keys"),
            ("DEPLOYMENT_CHECKLIST.md", "Pre-deployment checks"),
        ]
        
        print("\nAvailable guides:")
        for i, (file, desc) in enumerate(guides, 1):
            print(f"  {i}. {desc} ({file})")
        
        choice = input("\nSelect guide (1-5) or press Enter to skip: ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(guides):
            guide_file = guides[int(choice)-1][0]
            guide_path = self.root_dir / guide_file
            
            if guide_path.exists():
                if self.is_windows:
                    os.startfile(str(guide_path))
                elif self.is_mac:
                    subprocess.run(['open', str(guide_path)])
                else:
                    subprocess.run(['xdg-open', str(guide_path)])
                print(f"✅ Opening {guide_file}")
            else:
                print(f"❌ {guide_file} not found")
    
    def development_mode(self):
        """Development setup"""
        print("\n🛠️ DEVELOPMENT MODE")
        print("="*70)
        
        script = 'setup.bat' if self.is_windows else 'setup.sh'
        script_path = self.root_dir / script
        
        if script_path.exists():
            if self.is_windows:
                os.system(str(script_path))
            else:
                subprocess.run(['bash', str(script_path)])
        else:
            print(f"❌ {script} not found")
    
    def clean_build(self):
        """Clean build"""
        print("\n🧹 CLEAN BUILD")
        print("="*70)
        
        response = input("This will remove node_modules and venv. Continue? (y/n): ").strip().lower()
        if response != 'y':
            return
        
        # Remove backend venv
        backend_venv = self.root_dir / 'backend' / 'venv'
        if backend_venv.exists():
            print("Removing backend venv...")
            import shutil
            shutil.rmtree(backend_venv)
        
        # Remove frontend node_modules
        frontend_nm = self.root_dir / 'frontend' / 'node_modules'
        if frontend_nm.exists():
            print("Removing frontend node_modules...")
            import shutil
            shutil.rmtree(frontend_nm)
        
        print("✅ Clean build ready. Run 'Quick Start' to reinstall.")
    
    def git_operations(self):
        """Git operations"""
        print("\n📤 GIT OPERATIONS")
        print("="*70)
        
        print("\nGit status:")
        subprocess.run(['git', 'status'])
        
        response = input("\nCommit and push changes? (y/n): ").strip().lower()
        if response == 'y':
            message = input("Commit message: ").strip() or "deployment: automated update"
            subprocess.run(['git', 'add', '.'])
            subprocess.run(['git', 'commit', '-m', message])
            subprocess.run(['git', 'push', 'origin', 'main'])
            print("✅ Changes pushed to GitHub")
    
    def run(self):
        """Run the coordinator"""
        self.print_banner()
        
        while True:
            choice = self.menu()
            
            if choice == '1':
                self.quick_start()
            elif choice == '2':
                self.automated_deployment()
            elif choice == '3':
                self.health_check()
            elif choice == '4':
                self.manual_deployment()
            elif choice == '5':
                self.development_mode()
            elif choice == '6':
                self.clean_build()
            elif choice == '7':
                self.git_operations()
            elif choice == '8':
                print("\n👋 Goodbye!\n")
                sys.exit(0)
            else:
                print("❌ Invalid option")

if __name__ == '__main__':
    coordinator = DeploymentCoordinator()
    try:
        coordinator.run()
    except KeyboardInterrupt:
        print("\n\n👋 Cancelled")
        sys.exit(0)
