import requests
import json
import os

class ResumeImprover:
    def __init__(self):
        # FIXED: Now securely grabs the key from Hugging Face Settings
        self.api_key = os.getenv("GEMINI_API_KEY")
        # Updated to the standard, stable Gemini Flash model
        self.model = "gemini-3-flash-preview" 
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"

    def generate_bullets(self, missing_skills, job_description):
        if not self.api_key:
            return "⚠️ ERROR: GEMINI_API_KEY not found in Hugging Face Secrets!"
            
        if not missing_skills:
            return "No missing skills detected! Your resume is elite."

        prompt = f"""
        You are an elite technical recruiter. A candidate is applying for a job but is missing these skills: {', '.join(missing_skills)}.
        
        Context from Job Description:
        {job_description[:800]}
        
        Write 3 powerful, action-oriented resume bullet points that organically incorporate these missing skills. 
        Format them as a clean bulleted list. Do not include introductory text.
        """
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        try:
            response = requests.post(
                self.url, 
                headers={"Content-Type": "application/json"}, 
                json=payload
            )
            
            data = response.json()
            
            if response.status_code == 200:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                error_msg = data.get("error", {}).get("message", "Unknown API Error")
                return f"⚠️ API Error ({response.status_code}): {error_msg}"
                
        except Exception as e:
            return f"⚠️ System Error: {str(e)}"
