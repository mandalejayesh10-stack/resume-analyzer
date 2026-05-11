#!/usr/bin/env python3
"""
Resume Analyzer - Health Check & Verification Script
Verifies that backend and frontend are running correctly
"""

import requests
import json
import sys
import time
from pathlib import Path

class HealthChecker:
    def __init__(self, backend_url="http://localhost:8000", frontend_url="http://localhost:3000"):
        self.backend_url = backend_url.rstrip('/')
        self.frontend_url = frontend_url.rstrip('/')
        self.tests_passed = 0
        self.tests_failed = 0
        
    def print_section(self, title):
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    
    def check_backend_health(self):
        """Check if backend is running"""
        print(f"Checking backend at {self.backend_url}...")
        try:
            response = requests.get(f"{self.backend_url}/docs", timeout=5)
            if response.status_code == 200:
                print("✅ Backend is running and responsive")
                self.tests_passed += 1
                return True
            else:
                print(f"❌ Backend returned status {response.status_code}")
                self.tests_failed += 1
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to backend")
            print(f"   Make sure backend is running: uvicorn backend.main:app --reload")
            self.tests_failed += 1
            return False
        except Exception as e:
            print(f"❌ Backend check failed: {e}")
            self.tests_failed += 1
            return False
    
    def check_backend_endpoints(self):
        """Check if backend endpoints are working"""
        print("\nChecking backend endpoints...")
        
        endpoints = [
            ("Health Check", "GET", "/"),
            ("API Docs", "GET", "/docs"),
            ("ReDoc", "GET", "/redoc"),
        ]
        
        for name, method, endpoint in endpoints:
            try:
                url = f"{self.backend_url}{endpoint}"
                response = requests.get(url, timeout=5)
                if 200 <= response.status_code < 300:
                    print(f"  ✅ {name}: {endpoint}")
                    self.tests_passed += 1
                else:
                    print(f"  ❌ {name}: {endpoint} (status {response.status_code})")
                    self.tests_failed += 1
            except Exception as e:
                print(f"  ❌ {name}: {endpoint} ({e})")
                self.tests_failed += 1
    
    def check_frontend_health(self):
        """Check if frontend is running"""
        print(f"\nChecking frontend at {self.frontend_url}...")
        try:
            response = requests.get(self.frontend_url, timeout=5)
            if response.status_code == 200:
                print("✅ Frontend is running and responsive")
                self.tests_passed += 1
                return True
            else:
                print(f"❌ Frontend returned status {response.status_code}")
                self.tests_failed += 1
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to frontend")
            print(f"   Make sure frontend is running: npm run dev (in frontend directory)")
            self.tests_failed += 1
            return False
        except Exception as e:
            print(f"❌ Frontend check failed: {e}")
            self.tests_failed += 1
            return False
    
    def test_file_upload_endpoint(self):
        """Test file upload endpoint"""
        print("\nTesting file upload endpoint...")
        
        try:
            # Create a test file
            test_content = b"Test resume content\nExperience: 5 years\nSkills: Python, JavaScript"
            files = {'file': ('test_resume.txt', test_content)}
            
            response = requests.post(
                f"{self.backend_url}/upload",
                files=files,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'resume_id' in data:
                    print(f"  ✅ File upload working")
                    print(f"     Resume ID: {data.get('resume_id')}")
                    self.tests_passed += 1
                    return True
                else:
                    print(f"  ❌ File upload response missing resume_id")
                    print(f"     Response: {data}")
                    self.tests_failed += 1
            else:
                print(f"  ❌ File upload failed with status {response.status_code}")
                self.tests_failed += 1
                
        except Exception as e:
            print(f"  ❌ File upload test failed: {e}")
            self.tests_failed += 1
        
        return False
    
    def test_analyze_endpoint(self):
        """Test analyze endpoint"""
        print("\nTesting analyze endpoint...")
        
        try:
            test_resume = {
                "resume_text": "John Doe\n5 years of Python development\nSkills: Python, FastAPI, PostgreSQL"
            }
            
            response = requests.post(
                f"{self.backend_url}/analyze",
                json=test_resume,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'score' in data and 'ats_score' in data:
                    print(f"  ✅ Analyze endpoint working")
                    print(f"     Score: {data.get('score')}")
                    print(f"     ATS Score: {data.get('ats_score')}")
                    self.tests_passed += 1
                    return True
                else:
                    print(f"  ❌ Analyze response missing expected fields")
                    print(f"     Response keys: {list(data.keys())}")
                    self.tests_failed += 1
            else:
                print(f"  ❌ Analyze failed with status {response.status_code}")
                self.tests_failed += 1
                
        except Exception as e:
            print(f"  ❌ Analyze test failed: {e}")
            self.tests_failed += 1
        
        return False
    
    def check_cors_configuration(self):
        """Check if CORS is configured"""
        print("\nChecking CORS configuration...")
        
        try:
            response = requests.options(f"{self.backend_url}/", timeout=5)
            headers = response.headers
            
            cors_headers = {
                'access-control-allow-origin': headers.get('access-control-allow-origin'),
                'access-control-allow-methods': headers.get('access-control-allow-methods'),
                'access-control-allow-headers': headers.get('access-control-allow-headers'),
            }
            
            if cors_headers.get('access-control-allow-origin'):
                print(f"  ✅ CORS enabled")
                print(f"     Origin: {cors_headers['access-control-allow-origin']}")
                self.tests_passed += 1
            else:
                print(f"  ⚠️ CORS headers not found (may be normal)")
                
        except Exception as e:
            print(f"  ⚠️ CORS check failed: {e}")
    
    def run_all_checks(self):
        """Run all health checks"""
        self.print_section("Resume Analyzer - Health Check")
        
        print("Checking application health...\n")
        
        # Backend checks
        print("📊 BACKEND CHECKS")
        print("-" * 60)
        backend_running = self.check_backend_health()
        if backend_running:
            self.check_backend_endpoints()
            self.check_cors_configuration()
        
        # Frontend checks
        print("\n📊 FRONTEND CHECKS")
        print("-" * 60)
        frontend_running = self.check_frontend_health()
        
        # Integration tests (only if backend is running)
        if backend_running:
            print("\n📊 INTEGRATION TESTS")
            print("-" * 60)
            self.test_file_upload_endpoint()
            self.test_analyze_endpoint()
        
        # Summary
        self.print_section("Health Check Summary")
        
        total_tests = self.tests_passed + self.tests_failed
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {self.tests_passed}")
        print(f"❌ Failed: {self.tests_failed}")
        
        success_rate = (self.tests_passed / total_tests * 100) if total_tests > 0 else 0
        print(f"Success Rate: {success_rate:.1f}%")
        
        if self.tests_failed == 0 and backend_running and frontend_running:
            print("\n✨ All checks passed! Your application is healthy.")
            return 0
        elif self.tests_failed == 0:
            print("\n⚠️ Some services may not be running. Check startup commands.")
            return 1
        else:
            print(f"\n❌ {self.tests_failed} checks failed. See above for details.")
            return 1

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Health check for Resume Analyzer')
    parser.add_argument('--backend', default='http://localhost:8000', 
                       help='Backend URL')
    parser.add_argument('--frontend', default='http://localhost:3000',
                       help='Frontend URL')
    
    args = parser.parse_args()
    
    checker = HealthChecker(args.backend, args.frontend)
    sys.exit(checker.run_all_checks())
