#!/usr/bin/env python3
"""
Resume Analyzer - Interactive Deployment Automation
This script automates the entire deployment process
"""

import os
import sys
import json
import subprocess
from pathlib import Path

class Colors:
    """ANSI color codes"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'

class DeploymentAutomation:
    def __init__(self):
        self.root_dir = Path.cwd()
        self.secrets = {}
        
    def print_header(self, title):
        """Print a formatted header"""
        print(f"\n{Colors.BLUE}{'='*50}{Colors.END}")
        print(f"{Colors.BLUE}{title:^50}{Colors.END}")
        print(f"{Colors.BLUE}{'='*50}{Colors.END}\n")
    
    def print_success(self, msg):
        """Print success message"""
        print(f"{Colors.GREEN}✅ {msg}{Colors.END}")
    
    def print_error(self, msg):
        """Print error message"""
        print(f"{Colors.RED}❌ {msg}{Colors.END}")
    
    def print_warning(self, msg):
        """Print warning message"""
        print(f"{Colors.YELLOW}⚠️ {msg}{Colors.END}")
    
    def print_info(self, msg):
        """Print info message"""
        print(f"{Colors.CYAN}ℹ️ {msg}{Colors.END}")
    
    def check_prerequisites(self):
        """Check if all required tools are installed"""
        self.print_header("Step 1: Checking Prerequisites")
        
        tools = {
            'python3' if sys.platform != 'win32' else 'python': 'Python 3',
            'git': 'Git',
            'node': 'Node.js'
        }
        
        missing = []
        for cmd, name in tools.items():
            result = subprocess.run(
                ['where' if sys.platform == 'win32' else 'which', cmd],
                capture_output=True
            )
            if result.returncode == 0:
                self.print_success(f"{name} found")
            else:
                self.print_error(f"{name} not found")
                missing.append(name)
        
        if missing:
            print(f"\n{Colors.RED}Please install: {', '.join(missing)}{Colors.END}")
            sys.exit(1)
    
    def setup_backend(self):
        """Setup backend environment"""
        self.print_header("Step 2: Setting Up Backend")
        
        backend_dir = self.root_dir / 'backend'
        venv_dir = backend_dir / ('venv' if sys.platform != 'win32' else 'venv')
        
        # Create virtual environment
        if not venv_dir.exists():
            print("Creating Python virtual environment...")
            subprocess.run([sys.executable, '-m', 'venv', str(venv_dir)], check=True)
        
        # Get activation script
        if sys.platform == 'win32':
            activate_script = venv_dir / 'Scripts' / 'activate.bat'
        else:
            activate_script = venv_dir / 'bin' / 'activate'
        
        # Install dependencies
        print("Installing Python dependencies...")
        pip_exe = venv_dir / ('Scripts' if sys.platform == 'win32' else 'bin') / ('pip' if sys.platform == 'win32' else 'pip3')
        subprocess.run([str(pip_exe), 'install', '-q', '-r', 'requirements.txt'], 
                      cwd=str(backend_dir), check=True)
        
        # Create .env if it doesn't exist
        env_file = backend_dir / '.env'
        if not env_file.exists():
            print("Creating backend .env file...")
            env_file.write_text("""OPENAI_API_KEY=
DATABASE_URL=sqlite:///./resume_analyzer.db
CORS_ORIGINS=*
""")
        
        self.print_success("Backend setup complete")
    
    def setup_frontend(self):
        """Setup frontend environment"""
        self.print_header("Step 3: Setting Up Frontend")
        
        frontend_dir = self.root_dir / 'frontend'
        
        # Install dependencies
        print("Installing Node.js dependencies...")
        subprocess.run(['npm', 'install', '-q'], cwd=str(frontend_dir), check=True)
        
        # Create .env.local if it doesn't exist
        env_file = frontend_dir / '.env.local'
        if not env_file.exists():
            print("Creating frontend .env.local file...")
            env_file.write_text("NEXT_PUBLIC_API_URL=http://localhost:8000\n")
        
        self.print_success("Frontend setup complete")
    
    def verify_git(self):
        """Verify git repository"""
        self.print_header("Step 4: Verifying Git Repository")
        
        # Check if git repository
        result = subprocess.run(['git', 'rev-parse', '--git-dir'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            self.print_error("Not a git repository")
            sys.exit(1)
        
        self.print_success("Git repository found")
        
        # Commit any uncommitted changes
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            self.print_warning("Uncommitted changes found, committing...")
            subprocess.run(['git', 'add', '.'], check=False)
            subprocess.run(['git', 'commit', '-m', 'deployment: automated setup'], 
                         check=False)
    
    def setup_github_secrets(self):
        """Guide user through GitHub secrets setup"""
        self.print_header("Step 5: GitHub Secrets Setup")
        
        secrets_info = {
            'RENDER_API_KEY': 'https://dashboard.render.com/account/api-tokens',
            'RENDER_SERVICE_ID': 'https://dashboard.render.com (from service URL)',
            'VERCEL_TOKEN': 'https://vercel.com/account/tokens',
            'VERCEL_ORG_ID': 'https://vercel.com/account/settings',
            'VERCEL_PROJECT_ID': 'https://vercel.com/dashboard',
            'OPENAI_API_KEY': 'https://platform.openai.com/api-keys (optional)'
        }
        
        print("You need to add these secrets to your GitHub repository:")
        print(f"\nGo to: {Colors.CYAN}https://github.com/yourusername/resume-analyzer/settings/secrets/actions{Colors.END}\n")
        
        for secret, source in secrets_info.items():
            print(f"{Colors.YELLOW}{secret}{Colors.END}")
            print(f"  Source: {source}\n")
        
        input(f"{Colors.YELLOW}Press Enter after adding all secrets...{Colors.END}")
    
    def push_to_github(self):
        """Push changes to GitHub"""
        self.print_header("Step 6: Pushing to GitHub")
        
        # Show current branch
        result = subprocess.run(['git', 'branch', '--show-current'], 
                              capture_output=True, text=True)
        current_branch = result.stdout.strip()
        print(f"Current branch: {Colors.CYAN}{current_branch}{Colors.END}")
        
        response = input(f"\n{Colors.YELLOW}Push to GitHub? (y/n): {Colors.END}")
        if response.lower() == 'y':
            print("Pushing to GitHub...")
            result = subprocess.run(['git', 'push', 'origin', current_branch], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                self.print_success("Pushed to GitHub")
            else:
                self.print_error("Push failed")
                print(result.stderr)
        else:
            print("Push cancelled")
    
    def show_next_steps(self):
        """Show next steps"""
        self.print_header("Step 7: Deployment Complete")
        
        self.print_success("All setup complete!")
        print(f"\n{Colors.CYAN}🎉 Your app will be live in 5-10 minutes!{Colors.END}\n")
        
        print("Watch deployment at:")
        print(f"  {Colors.YELLOW}https://github.com/yourusername/resume-analyzer/actions{Colors.END}")
        print("\nCheck status at:")
        print(f"  {Colors.YELLOW}Render: https://dashboard.render.com{Colors.END}")
        print(f"  {Colors.YELLOW}Vercel: https://vercel.com/dashboard{Colors.END}")
    
    def run(self):
        """Run the complete deployment automation"""
        try:
            self.check_prerequisites()
            self.setup_backend()
            self.setup_frontend()
            self.verify_git()
            self.setup_github_secrets()
            self.push_to_github()
            self.show_next_steps()
            
            print(f"\n{Colors.GREEN}✨ Deployment automation complete!{Colors.END}\n")
            
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Cancelled by user{Colors.END}")
            sys.exit(0)
        except Exception as e:
            self.print_error(f"Unexpected error: {e}")
            sys.exit(1)

if __name__ == '__main__':
    automator = DeploymentAutomation()
    automator.run()
