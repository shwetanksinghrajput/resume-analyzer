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
            
        skills_path = os.path.join("data", "skills.json")
        with open(skills_path, "r", encoding="utf-8") as f:
            self.skills_db = json.load(f)

    def extract_skills(self, text):
        if not text:
            return set()
            
        text_content = text.lower()
        found_skills = set()
        
        for skill in self.skills_db:
            clean_skill = skill.lower().strip()
            
            # PASS 1: Strict Regex (Fastest and safest)
            pattern = r'\b' + re.escape(clean_skill) + r'\b'
            if re.search(pattern, text_content):
                found_skills.add(skill)
                continue
                
            # PASS 2: Fuzzy Matching (For misspellings & variations)
            # Only apply fuzzy math to words longer than 3 letters to avoid 
            # falsely matching languages like "C", "R", or "Go"
            if len(clean_skill) > 3:
                # partial_ratio checks if the skill string is "embedded" in the text
                if fuzz.partial_ratio(clean_skill, text_content) >= 90:
                    found_skills.add(skill)
                
        return found_skills