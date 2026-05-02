import spacy
import json
import os
import re
from thefuzz import fuzz

class ResumeProcessor:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            os.system("python -m spacy download en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")
            
        skills_path = "skills.json" 
        with open(skills_path, "r", encoding="utf-8") as f:
            self.skills_db = json.load(f)

    def extract_skills(self, text):
        if not text:
            return set()
            
        text_content = text.lower()
        found_skills = set()
        
        for skill in self.skills_db:
            clean_skill = skill.lower().strip()
            
            pattern = r'\b' + re.escape(clean_skill) + r'\b'
            if re.search(pattern, text_content):
                found_skills.add(skill)
                continue
                
            if len(clean_skill) > 3:
                if fuzz.partial_ratio(clean_skill, text_content) >= 90:
                    found_skills.add(skill)
                
        return found_skills
