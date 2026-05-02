import requests
import json
import streamlit as st # <-- Make sure this is imported

class ResumeImprover:
    def __init__(self):
        # This tells the app to look for the key in the cloud's secure vault
        try:
            self.api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            self.api_key = None 
            
        self.model = "gemini-3-flash-preview"
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"

        
    def generate_bullets(self, missing_skills, job_description):
        if self.api_key == "PASTE_YOUR_REAL_KEY_HERE":
            return "⚠️ ERROR: You need to paste your actual API key into engine/improver.py!"
            
        if not missing_skills:
            return "No missing skills detected! Your resume is elite."

        prompt = f"""
        You are an elite technical recruiter. A candidate is applying for a job but is missing these skills: {', '.join(missing_skills)}.
        
        Context from Job Description:
        {job_description[:800]}
        
        Write 3 powerful, action-oriented resume bullet points that organically incorporate these missing skills. 
        Format them as a clean bulleted list. Do not include introductory text.
        """
        
        # Formatting the payload exactly how the REST API expects it
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
            
            # If the call is successful, extract the text
            if response.status_code == 200:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                # If Google throws an error, show exactly what they said
                error_msg = data.get("error", {}).get("message", "Unknown API Error")
                return f"⚠️ API Error ({response.status_code}): {error_msg}"
                
        except Exception as e:
            return f"⚠️ System Error: {str(e)}"
