import os
import json
from pathlib import Path

class Config:
    def __init__(self):
        self.config_file = "user_config.json"
        self.resume_path = "resume.pdf"
        
    def setup_user_credentials(self):
        """Interactive setup for user credentials"""
        print("🔧 Setting up your job application credentials...")
        
        config = {}
        
        # Personal Information
        print("\n📋 Personal Information:")
        config['personal'] = {
            'full_name': input("Full Name: "),
            'email': input("Email: "),
            'phone': input("Phone: "),
            'linkedin': input("LinkedIn URL (optional): "),
            'github': input("GitHub URL (optional): "),
            'location': input("Current Location: ")
        }
        
        # Job Platforms Credentials
        print("\n🔐 Job Platform Credentials:")
        
        # RemoteOK (usually doesn't require login for applications)
        config['platforms'] = {}
        
        # Twitter/X
        print("\nTwitter/X (for X Jobs):")
        config['platforms']['twitter'] = {
            'email': input("Twitter/X Email: "),
            'password': input("Twitter/X Password: ")
        }
        
        # Turing
        print("\nTuring (for remote developer jobs):")
        config['platforms']['turing'] = {
            'email': input("Turing Email: "),
            'password': input("Turing Password: ")
        }
        
        # Indeed
        print("\nIndeed:")
        config['platforms']['indeed'] = {
            'email': input("Indeed Email: "),
            'password': input("Indeed Password: ")
        }
        
        # Dice
        print("\nDice:")
        config['platforms']['dice'] = {
            'email': input("Dice Email: "),
            'password': input("Dice Password: ")
        }
        
        # Job Preferences
        print("\n🎯 Job Preferences:")
        config['preferences'] = {
            'job_titles': [
                "DevOps Engineer", "Cloud Engineer", "Site Reliability Engineer (SRE)",
                "Infrastructure Engineer", "Platform Engineer", "AWS Engineer",
                "Kubernetes Administrator", "CI/CD Engineer", "Linux Systems Engineer",
                "Cloud Automation Engineer", "Junior DevOps Associate", "Remote DevOps Intern"
            ],
            'skills': ["DevOps", "AWS", "Docker", "Kubernetes", "Python", "Linux", "CI/CD", "Jenkins", "Terraform"],
            'salary_min': input("Minimum Salary (optional): "),
            'remote_only': input("Remote jobs only? (y/n): ").lower() == 'y',
            'experience_level': input("Experience Level (entry/mid/senior): ")
        }
        
        # Save config
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print("✅ Configuration saved successfully!")
        return config
    
    def load_config(self):
        """Load existing configuration"""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ No configuration found. Running setup...")
            return self.setup_user_credentials()
    
    def update_resume_path(self, new_path):
        """Update resume file path"""
        if os.path.exists(new_path):
            # Copy resume to bot directory
            import shutil
            shutil.copy2(new_path, self.resume_path)
            print(f"✅ Resume copied to {self.resume_path}")
            return True
        else:
            print(f"❌ Resume file not found: {new_path}")
            return False
