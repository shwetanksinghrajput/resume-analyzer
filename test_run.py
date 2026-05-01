from engine.extractor import extract_text_from_pdf
from engine.processor import ResumeProcessor
from engine.matcher import ResumeMatcher

# 1. Setup the inputs
pdf_file = "resume.pdf" 
dummy_job_description = """
We are looking for a Software Engineer with strong experience in Python, Java, 
and building REST APIs. The ideal candidate will have hands-on experience with 
Docker, Kubernetes, and Cloud platforms like AWS. Familiarity with Agile 
methodologies and strong Problem Solving skills are required. DSA knowledge is a plus.
"""

print("🚀 Extracting text from PDF...")
resume_text = extract_text_from_pdf(pdf_file)

print("🧠 Firing up the NLP Processor...")
processor = ResumeProcessor()

print("🔍 Analyzing Resume and Job Description...")
# Extract skills from BOTH the resume and the Job Description
resume_skills = processor.extract_skills(resume_text)
jd_skills = processor.extract_skills(dummy_job_description)

print("⚖️ Calculating Match Score...")
# Compare them using our new Matcher
matcher = ResumeMatcher()
score, missing, matched = matcher.calculate_match(resume_skills, jd_skills)

# --- DISPLAY THE FINAL DASHBOARD ---
print("\n" + "="*40)
print(f"🎯 FINAL MATCH SCORE: {score}%")
print("="*40)

print(f"\n✅ MATCHED SKILLS ({len(matched)}):")
for skill in matched:
    print(f"  - {skill.title()}") # .title() capitalizes the first letter for display

print(f"\n❌ MISSING SKILLS ({len(missing)}):")
for skill in missing:
    print(f"  - {skill.title()}")

print("\n" + "="*40)